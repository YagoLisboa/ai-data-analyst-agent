
from agents.sql_agent import generate_sql
from agents.analysis_agent import explain_result
from utils.database_utils import run_query

def main():
    print("AI Data Analyst Agent")
    print("---------------------")

    question = input("Ask a question about the dataset: ")

    sql_query = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql_query)

    result = run_query(sql_query)

    print("\nQuery Result:")
    print(result)

    explanation = explain_result(question, result)

    print("\nAI Explanation:")
    print(explanation)

if __name__ == "__main__":
    main()
