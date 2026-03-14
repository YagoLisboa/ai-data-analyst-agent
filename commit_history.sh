#!/bin/bash

echo "Initializing repository..."

git init

echo "Commit 1 - project structure"
git add .
git commit -m "initial project structure for AI Data Analyst Agent"

sleep 2

echo "Commit 2 - dataset"
git add data/
git commit -m "add sales dataset for testing SQL agent"

sleep 2

echo "Commit 3 - database script"
git add database/
git commit -m "add SQLite database creation script"

sleep 2

echo "Commit 4 - SQL agent"
git add agents/sql_agent.py
git commit -m "implement natural language to SQL generation agent"

sleep 2

echo "Commit 5 - analysis agent"
git add agents/analysis_agent.py
git commit -m "implement AI result explanation agent"

sleep 2

echo "Commit 6 - database utilities"
git add utils/
git commit -m "add database query utility functions"

sleep 2

echo "Commit 7 - main interface"
git add main.py
git commit -m "create CLI interface for AI data analysis agent"

sleep 2

echo "Commit 8 - streamlit app"
git add streamlit_app.py
git commit -m "add Streamlit interface for interactive data analysis"

sleep 2

echo "Commit 9 - documentation"
git add README.md
git commit -m "add project documentation"

sleep 2

echo "Commit 10 - requirements"
git add requirements.txt
git commit -m "add project dependencies"

echo "Connecting to GitHub..."
git remote add origin https://github.com/YagoLisboa/ai-data-analyst-agent.git
git branch -M main
git push -u origin main

echo "All commits created and pushed to GitHub successfully."