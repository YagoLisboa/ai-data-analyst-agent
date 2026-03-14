
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_sql(question):

    prompt = f"""
You are a data analyst.

Convert the following natural language question into SQL.

Table name: sales

Columns:
order_id
product
price
quantity
date
region

Question: {question}

Return only SQL.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
