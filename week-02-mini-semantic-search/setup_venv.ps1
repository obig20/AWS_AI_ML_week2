# Week 2 - Mini Semantic Search Lab
# Setup script for Windows PowerShell

Write-Host "Creating virtual environment..." -ForegroundColor Green
python -m venv .venv

Write-Host "Activating virtual environment..." -ForegroundColor Green
.\.venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..." -ForegroundColor Green
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "Run: jupyter notebook notebooks/mini_semantic_search.ipynb" -ForegroundColor Yellow
