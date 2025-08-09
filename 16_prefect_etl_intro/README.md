# 🛠️ Data Engineering with Prefect — Simple ETL Pipeline

This module demonstrates how to use **Prefect 2.0** to build a simple ETL pipeline in Python.

---

## 🎯 Goal

Create a daily ETL flow that:
1. Extracts data from a local CSV file
2. Cleans and transforms it using `pandas`
3. Saves the result to a new file
4. Is fully tracked and orchestrated by Prefect

---

## 🧰 Tools & Libraries

- Python
- [Prefect 2.0](https://docs.prefect.io/)
- pandas

---

## 🚀 How to Run

1. **Install dependencies**
```bash
pip install prefect pandas
Project structure

16_prefect_etl_intro/
├── task.md
├── etl_prefect_pipeline.py
├── explanation.md
└── README.md

Prepare input file

Create a folder data/ and a file source_data.csv:

Month,Revenue
Jan,1000
Feb,1500
Mar,1200
Apr,1700
May,2000
Run the pipeline

python etl_prefect_pipeline.py

🧠 Key Concepts Demonstrated

Concept	Description
@task	Wraps a Python function into a Prefect task
@flow	Orchestrates multiple tasks
Logging	Track progress using print() (can use logger)
Parameters	Can easily parameterize input/output paths

✅ Output

A file data/final_data.csv with an additional column:

Revenue_with_Tax = Revenue * 1.2
