import sqlite3
import pandas as pd
import streamlit as st
from openai import OpenAI
import ollama
import requests

st.set_page_config(page_title="LLM Data Analyst Assistant", layout="wide")
st.title("📊 LLM Data Analyst Assistant")
st.caption("Upload CSV/Excel → Ask questions → Get SQL + results")

# API key input (safe: type password)
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# Upload local file from your computer
uploaded = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if not uploaded:
    st.info("👆 Upload a file to start.")
    st.stop()

# Read file
if uploaded.name.endswith(".csv"):
    def read_csv_safely(uploaded_file):
        for enc in ["utf-8", "utf-8-sig", "cp1252", "latin1", "utf-16"]:
            try:
                uploaded_file.seek(0)
                return pd.read_csv(uploaded_file, encoding=enc)
            except UnicodeDecodeError:
                continue
            uploaded_file.seek(0)
            return pd.read_csv(uploaded_file, encoding="latin1", errors="replace")

if uploaded.name.endswith(".csv"):
    df = read_csv_safely(uploaded)
else:
    df = pd.read_excel(uploaded)

    
st.subheader("Dataset Preview")
st.dataframe(df.head(25), use_container_width=True)

# Load into SQLite in-memory database
conn = sqlite3.connect(":memory:")
table_name = "data"
df.to_sql(table_name, conn, index=False, if_exists="replace")

def question_to_sql(question, columns):
    prompt = f"""
You are a senior data analyst.
Convert the question into SQLite SQL.

Table name: data
Columns: {columns}

Return ONLY SQL query.

Question: {question}
"""

    response = ollama.chat(
        model="gemma3:4b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
st.subheader("Ask a Question")
question = st.text_input("Example: Top 5 customers by sales, total revenue by month, etc.")

col1, col2 = st.columns([1, 1])
run = col1.button("🔎 Generate SQL + Run")
show_cols = col2.button("📌 Show Columns")

if show_cols:
    st.write("Columns:", list(df.columns))

if run:
    if not question.strip():
        st.warning("Type a question first.")
        st.stop()

    try:
        sql = question_to_sql(question, df.columns.tolist())
        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        result = pd.read_sql_query(sql, conn)
        st.subheader("Result")
        st.dataframe(result, use_container_width=True)

        # Quick chart if numeric columns exist
        numeric_cols = result.select_dtypes(include=["number"]).columns.tolist()
        if numeric_cols:
            st.subheader("Quick Chart")
            st.line_chart(result[numeric_cols])

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.info("Try a more specific question like: 'Total sales by month' or 'Top 10 products by revenue'.")
