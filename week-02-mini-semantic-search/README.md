# Week 2 Mini Semantic Search Lab

## Project Overview
This project implements a Mini Semantic Search engine for FAQs. It loads FAQ data from CSV/JSON, cleans it using multiple Python functions, performs NumPy-based statistical analysis, converts text to embeddings using Sentence Transformers, stores them in ChromaDB, and retrieves the top 3 most semantically similar FAQs for a user query.

## Features
- Load raw FAQ data using Pandas (CSV/JSON)
- Data cleaning with 5+ functions (missing values, duplicates, normalization, dtypes, outlier detection)
- NumPy calculations (mean, median, std, percentiles, etc.)
- Text embeddings with Sentence Transformers
- Vector storage and search with ChromaDB
- Interactive Jupyter notebook with full pipeline
- Colab-compatible with relative paths
- Clean, organized project structure

## Folder Structure
`
week-02-mini-semantic-search/
├── data/
│   ├── raw_faq.csv
│   └── raw_faq.json
├── notebooks/
│   └── mini_semantic_search.ipynb
├── src/
│   ├── cleaning.py
│   ├── numpy_stats.py
│   └── semantic_search.py
├── utils/
├── .gitignore
├── README.md
└── requirements.txt
`

## Installation

### Prerequisites
- Python 3.8+
- pip

### Create and Activate Virtual Environment

**Windows (PowerShell):**
`powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
`

**Windows (Command Prompt):**
`cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
`

**Linux/macOS:**
`ash
python3 -m venv .venv
source .venv/bin/activate
`

### Install Dependencies
`ash
pip install -r requirements.txt
`

## Running the Notebook
`ash
jupyter notebook notebooks/mini_semantic_search.ipynb
`
Or use JupyterLab:
`ash
jupyter lab notebooks/mini_semantic_search.ipynb
`

## How to Run Semantic Search
The notebook demonstrates the full pipeline. You can also use the classes in src/ directly:
`python
from src.semantic_search import MiniSemanticSearch
searcher = MiniSemanticSearch()
searcher.add_documents(cleaned_df)
results = searcher.search('What is AI?')
`

## Example Queries and Expected Result Format
Example query: "What is machine learning?"
Results include:
- Matched questions
- Matched answers
- Similarity/distance scores from ChromaDB

## Google Colab Instructions
1. Upload the notebook to Google Colab
2. Upload data/ folder and src/ folder, or clone from GitHub
3. Install dependencies: !pip install -r requirements.txt
4. Use relative paths (already configured) - paths work from notebook location
5. Note: Colab link not provided as it's not pre-created; upload manually

## Notes
- Uses ll-MiniLM-L6-v2 sentence transformer model (downloads on first run)
- ChromaDB persists to ./chroma_db/ directory
- All paths use relative paths for portability
