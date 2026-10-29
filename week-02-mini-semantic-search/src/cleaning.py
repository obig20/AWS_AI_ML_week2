import pandas as pd
import numpy as np
import re

def load_raw_data(filepath):
    '''Load raw FAQ data from CSV or JSON file using Pandas.'''
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.json'):
        df = pd.read_json(filepath)
        if isinstance(df, dict):
            for key in df:
                if isinstance(df[key], list):
                    df = pd.DataFrame(df[key])
                    break
    else:
        raise ValueError('Unsupported file format. Use CSV or JSON.')
    return df

def handle_missing_values(df):
    '''Handle missing values by dropping rows where question or answer is missing/empty.'''
    df = df.copy()
    if 'question' in df.columns:
        df['question'] = df['question'].fillna('')
    if 'answer' in df.columns:
        df['answer'] = df['answer'].fillna('')
    df = df[(df['question'].astype(str).str.strip() != '') & (df['answer'].astype(str).str.strip() != '')]
    return df

def remove_duplicates(df):
    '''Remove duplicate records based on question and answer.'''
    df = df.copy()
    df = df.drop_duplicates(subset=['question', 'answer'], keep='first')
    return df

def normalize_text_case_whitespace(df):
    '''Normalize text case and whitespace for question and answer columns.'''
    df = df.copy()
    for col in ['question', 'answer']:
        if col in df.columns:
            df[col] = df[col].astype(str)
            df[col] = df[col].str.strip()
            df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
            df[col] = df[col].str.lower()
    return df

def convert_to_appropriate_dtypes(df):
    '''Convert relevant columns to appropriate data types.'''
    df = df.copy()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str)
    return df

def detect_handle_outliers(df):
    '''Flag/detect outliers: empty, extremely short, or unusually long FAQ records.'''
    df = df.copy()
    df['q_len'] = df['question'].astype(str).apply(len)
    df['a_len'] = df['answer'].astype(str).apply(len)
    q_mean = df['q_len'].mean()
    q_std = df['q_len'].std() if df['q_len'].std() > 0 else 0
    a_mean = df['a_len'].mean()
    a_std = df['a_len'].std() if df['a_len'].std() > 0 else 0
    def is_outlier(row):
        ql, al = row['q_len'], row['a_len']
        if ql < 5 or al < 5:
            return True
        if q_std > 0 and abs(ql - q_mean) > 3 * q_std:
            return True
        if a_std > 0 and abs(al - a_mean) > 3 * a_std:
            return True
        if ql > 200 or al > 1000:
            return True
        return False
    df['is_outlier'] = df.apply(is_outlier, axis=1)
    df_clean = df[~df['is_outlier']].copy()
    df_clean = df_clean.drop(columns=['q_len', 'a_len', 'is_outlier'])
    return df_clean
