📊 LLM Data Analyst Assistant

An AI-powered Data Analyst Assistant that converts natural language questions into SQL queries and generates real-time insights from CSV/Excel datasets.

Built using:

🐍 Python

📈 Streamlit

🗄 SQLite

🤖 Local LLM (Ollama – gemma3)

🚀 Overview

This project allows users to:

Upload a CSV or Excel dataset

Ask business questions in plain English

Automatically generate SQL queries

Execute queries on structured data

Visualize results instantly

Example queries:

Top 5 customers by sales

Total revenue by month

Average order value

Sales by region

Monthly growth trend

🧠 How It Works

User Question
→ LLM converts question to SQL
→ SQLite executes SQL
→ Streamlit displays results
→ Automatic visualization

This eliminates the need to manually write SQL queries.

🛠 Tech Stack
Layer	Technology
UI	Streamlit
Data Processing	Pandas
Database	SQLite (in-memory)
LLM	Ollama (gemma3 local model)
Visualization	Streamlit charts
💻 Installation
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/LLM-Data-Analyst-Assistant.git
cd LLM-Data-Analyst-Assistant

2️⃣ Install Dependencies
pip install streamlit pandas openpyxl requests

3️⃣ Install Ollama (Local LLM)

Download from:

https://ollama.com/download

Make sure Ollama Desktop is running.

4️⃣ Ensure Model is Available

Use an installed model such as:

gemma3:4b


Check available models:

Invoke-RestMethod http://localhost:11434/api/tags

5️⃣ Run the App
streamlit run app.py

📂 Project Structure
LLM-Data-Analyst-Assistant/
│
├── app.py
├── README.md
├── requirements.txt
└── sample_data/

📊 Example Use Case

Business Manager asks:

Which customer generated the highest revenue this quarter?

The assistant:

Converts question into SQL

Aggregates data

Sorts by revenue

Returns top customer instantly