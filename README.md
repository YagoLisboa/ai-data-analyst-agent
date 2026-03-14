
# AI Data Analyst Agent

This project demonstrates how a Generative AI agent can analyze structured data using SQL.

## Features
- Natural language questions
- Automatic SQL generation
- SQL execution on a database
- AI-powered explanation of results

## Technologies
- Python
- SQL (SQLite)
- Pandas
- OpenAI API
- AI Agents

## Example Questions

- Which region generated the highest revenue?
- What are the top 5 best-selling products?
- What is the total revenue?
- Which product sold the most units?

## How it works

User Question → LLM Agent → SQL Generation → Database Query → AI Explanation

## Setup

1. Install dependencies:

pip install -r requirements.txt

2. Add your OpenAI API key:

Create a .env file:

OPENAI_API_KEY=your_key_here

3. Run the project:

python main.py
