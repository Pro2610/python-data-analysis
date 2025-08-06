# 🌐 Airflow ETL Pipeline — Explanation

This script demonstrates a **basic ETL pipeline in Apache Airflow** using PythonOperator.

---

## ✅ Key Components:

### 1. **Default Arguments**

Define common settings for the DAG:
- `start_date`
- `retries`
- `retry_delay`

```python
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 8, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
2. DAG Definition

A DAG (Directed Acyclic Graph) organizes tasks and sets the schedule:

dag = DAG(
    'etl_csv_pipeline',
    default_args=default_args,
    description='Simple ETL pipeline with Airflow',
    schedule_interval='@daily',
    catchup=False
)
3. ETL Steps

Extract: Read data from source_data.csv

Transform: Add a calculated column Revenue_with_Tax

Load: Save final dataset to final_data.csv

4. PythonOperator

Each ETL step is defined as a Python function and executed by PythonOperator:

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag
)
5. Task Dependencies

Set the execution order:

Extract → Transform → Load

In Airflow:

extract_task >> transform_task >> load_task

✅ Result: Airflow runs a simple ETL pipeline daily and logs progress in the web interface.

🔍 Next Steps:

Replace CSV with a real database or API

Add data validation

Push data to data warehouse (BigQuery, Redshift)
