# 🧠 Explanation — Prefect ETL Pipeline

This example demonstrates how to build a simple ETL pipeline using **Prefect 2.0**.  
Prefect allows you to orchestrate tasks with better visibility, retry logic, and logging.

---

## 🔧 Structure:

### 1. `@task` decorators
Each step of the ETL process is defined as a separate function and decorated with `@task`.

```python
@task
def extract_data(file_path: str) -> pd.DataFrame:
    ...
This allows Prefect to:

Monitor execution

Track logs and outputs

Handle retries if needed

2. @flow decorator

The main pipeline is a function decorated with @flow.
It orchestrates all the tasks and defines the execution logic.

@flow
def run_etl_pipeline():
    ...
📥 Extract
Reads data from a local CSV file using pandas.read_csv.

df = pd.read_csv(file_path)
🔁 Transform

Drops missing rows

Adds a new column Revenue_with_Tax as Revenue * 1.2

df = df.dropna()
df['Revenue_with_Tax'] = df['Revenue'] * 1.2
📤 Load
Writes the cleaned DataFrame to a new CSV file:

df.to_csv(output_path, index=False)

▶️ Run the Flow

To execute the pipeline:

python etl_prefect_pipeline.py

Prefect will:

Show real-time logs

Track status of each task

Provide visibility in the UI (if connected)

💡 What You Can Add Next

Validation task: check row counts, nulls, types

Parameters: dynamic file paths or tax rates

Logging: use Prefect logger instead of print

Scheduled runs using Prefect Cloud or Prefect Orion
