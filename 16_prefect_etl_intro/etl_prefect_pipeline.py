from prefect import flow, task
import pandas as pd
import os

# ----------------------
# Task 1 — Extract
# ----------------------
@task
def extract_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    print("✅ Data extracted")
    return df

# ----------------------
# Task 2 — Transform
# ----------------------
@task
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df['Revenue_with_Tax'] = df['Revenue'] * 1.2
    print("🔧 Data transformed")
    return df

# ----------------------
# Task 3 — Load
# ----------------------
@task
def load_data(df: pd.DataFrame, output_path: str):
    df.to_csv(output_path, index=False)
    print(f"📁 Data saved to: {output_path}")

# ----------------------
# Flow
# ----------------------
@flow(name="Simple ETL with Prefect")
def run_etl_pipeline():
    input_path = "data/source_data.csv"
    output_path = "data/final_data.csv"

    df_raw = extract_data(input_path)
    df_cleaned = transform_data(df_raw)
    load_data(df_cleaned, output_path)

# ----------------------
# Entry point
# ----------------------
if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    run_etl_pipeline()
