# 📊 LLM Data Analyst Assistant  

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)  ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white) ![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge) ![LLM](https://img.shields.io/badge/LLM-gemma3-blue?style=for-the-badge)  

---

## 🚀 What is this?

An AI-powered **Data Analyst Assistant** that converts natural language questions into SQL queries and generates real-time insights from CSV/Excel datasets.

Instead of manually writing SQL queries, users can simply ask business questions in plain English — and the assistant automatically:

- Generates SQL queries  
- Executes them on structured data  
- Displays results instantly  
- Creates automatic visualizations  

---

## ✨ Features

✅ Upload CSV or Excel datasets  
✅ Ask business questions in plain English  
✅ Automatic SQL query generation  
✅ SQLite in-memory execution  
✅ Real-time data visualization  
✅ Local LLM integration (Ollama – gemma3)  
✅ No cloud API required  

---

## 🧠 How It Works

User Question  
→ LLM converts question to SQL  
→ SQLite executes SQL  
→ Streamlit displays results  
→ Automatic visualization generated  

This completely removes the need for manual SQL writing.

---

## 📊 Example Queries

- Top 5 customers by sales  
- Total revenue by month  
- Average order value  
- Sales by region  
- Monthly growth trend  

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| UI | Streamlit |
| Data Processing | Pandas |
| Database | SQLite (In-Memory) |
| LLM | Ollama (gemma3 local model) |
| Visualization | Streamlit Charts |

---

## 💻 Quick Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/LLM-Data-Analyst-Assistant.git
cd LLM-Data-Analyst-Assistant

```

2️⃣ **Install Dependencies**
``` bash
pip install streamlit pandas openpyxl requests
```

3️⃣ **Install Ollama (Local LLM)**

Download from:
``` bash
https://ollama.com/download
```

Make sure Ollama Desktop is running.

4️⃣ **Ensure Model is Available**

Use an installed model such as:
``` bash
gemma3:4b
```

Check available models:
``` bash
Invoke-RestMethod http://localhost:11434/api/tags
```

5️⃣ **Run the App**
``` bash
streamlit run app.py
```

Open in browser:

http://localhost:8501

📂 Project Structure
LLM-Data-Analyst-Assistant/
│
├── app.py
├── README.md
├── requirements.txt
└── sample_data/

📊 Example Use Case

👨‍💼 Business Manager asks:

Which customer generated the highest revenue this quarter?

The Assistant:

- Converts question into SQL

- Aggregates data

- Sorts by revenue

- Returns top customer instantly

- Displays a visualization

🎯 Why This Project?

- This project demonstrates:

- LLM + SQL integration

- Local AI deployment (No OpenAI API required)

- Real-time analytics

- Business intelligence automation

- Practical AI application for decision-making
