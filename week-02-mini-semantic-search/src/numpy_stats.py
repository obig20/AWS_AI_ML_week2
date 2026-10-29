import numpy as np
import pandas as pd

def compute_text_length_stats(df, text_col='question'):
    '''Compute mean, median, std, and percentiles of text length using NumPy.'''
    lengths = df[text_col].astype(str).apply(len).values
    stats = {
        'mean': float(np.mean(lengths)),
        'median': float(np.median(lengths)),
        'std': float(np.std(lengths, ddof=1)) if len(lengths) > 1 else 0.0,
        'p25': float(np.percentile(lengths, 25)),
        'p50': float(np.percentile(lengths, 50)),
        'p75': float(np.percentile(lengths, 75)),
        'p90': float(np.percentile(lengths, 90)),
        'min': float(np.min(lengths)),
        'max': float(np.max(lengths)),
        'count': int(len(lengths))
    }
    return stats, lengths
