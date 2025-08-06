from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

# ---------------------------
# 1. Default DAG arguments
# ---------------------------
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 8, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# ---------------------------
# 2. DAG Definition
# ---------------------------
dag = DAG(
    'etl_csv_pipeline',
    default_args=default_args,
    description='Simple ETL pipeline with Airflow',
    schedule_interval='@daily',
    catchup=False
)

# ---------------------------
# 3. Define Python tasks
# ---------------------------

def extract():
    df = pd.read_csv('/opt/airflow/dags/data/source_data.csv')
    df.to_csv('/opt/airflow/dags/temp/extracted_data.csv', index=False)
    print("✅ Extract completed")

def transform():
    df = pd.read_csv('/opt/airflow/dags/temp/extracted_data.csv')
    df['Revenue_with_Tax'] = df['Revenue'] * 1.2
    df.to_csv('/opt/airflow/dags/temp/transformed_data.csv', index=False)
    print("✅ Transform completed")

def load():
    df = pd.read_csv('/opt/airflow/dags/temp/transformed_data.csv')
    df.to_csv('/opt/airflow/dags/data/final_data.csv', index=False)
    print("✅ Load completed")

# ---------------------------
# 4. Create Tasks
# ---------------------------
extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag
)

# ---------------------------
# 5. Set Task Dependencies
# ---------------------------
extract_task >> transform_task >> load_task
