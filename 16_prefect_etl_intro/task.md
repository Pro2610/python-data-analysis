# 🛠️ Prefect ETL Pipeline — Intro

## 🎯 Goal:
Create a simple data pipeline using **Prefect 2.0**, simulating a basic ETL workflow.

---

## ✅ Steps:

1. **Extract** data from a CSV file
2. **Transform** data using `pandas`:
   - Clean columns
   - Add a calculated column
3. **Load** the final result into a new CSV file
4. Use Prefect to:
   - Create individual `@task` functions
   - Orchestrate them with a `@flow`
   - Run locally and track in Prefect UI (optional)

---

## 🧰 Tools:
- Python
- Prefect 2.0
- pandas

---

## 🧪 Extra Ideas (optional):
- Add logging to each task
- Parameterize file paths
- Add a step to validate row counts
