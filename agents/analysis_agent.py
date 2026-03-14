
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def explain_result(question, result):

    prompt = f"""
You are a data analyst.

User question:
{question}

Query result:
{result}

Explain the result in clear natural language.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
