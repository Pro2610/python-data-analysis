from __future__ import annotations
from typing import List
import pandas as pd
from prefect import flow, task, get_run_logger

# ----------------------
# Validation helpers
# ----------------------
@task
def validate_required_columns(df: pd.DataFrame, required: List[str]) -> pd.DataFrame:
    logger = get_run_logger()
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    logger.info("✅ Required columns present: %s", required)
    return df

@task
def validate_no_nulls(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    logger = get_run_logger()
    null_counts = df[cols].isna().sum()
    bad = null_counts[null_counts > 0]
    if not bad.empty:
        raise ValueError(f"Nulls found in columns: {bad.to_dict()}")
    logger.info("✅ No nulls in columns: %s", cols)
    return df

@task
def validate_numeric_nonnegative(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    logger = get_run_logger()
    for c in cols:
        if not pd.api.types.is_numeric_dtype(df[c]):
            raise TypeError(f"Column '{c}' must be numeric")
        if (df[c] < 0).any():
            raise ValueError(f"Negative values found in '{c}'")
    logger.info("✅ Numeric & non-negative check passed for: %s", cols)
    return df

@task
def validate_rowcount(df: pd.DataFrame, min_rows: int = 1) -> pd.DataFrame:
    logger = get_run_logger()
    if len(df) < min_rows:
        raise ValueError(f"Rowcount {len(df)} is less than minimum {min_rows}")
    logger.info("✅ Rowcount check passed: %d rows", len(df))
    return df

# ----------------------
# Core ETL tasks
# ----------------------
@task
def extract_csv(path: str) -> pd.DataFrame:
    logger = get_run_logger()
    df = pd.read_csv(path)
    logger.info("📥 Extracted %d rows from %s", len(df), path)
    return df

@task
def transform_add_tax(df: pd.DataFrame, tax_rate: float = 1.2) -> pd.DataFrame:
    logger = get_run_logger()
    df = df.copy()
    df['Revenue_with_Tax'] = (df['Revenue'] * tax_rate).round(2)
    logger.info("🔧 Added Revenue_with_Tax with tax_rate=%.2f", tax_rate)
    return df

@task
def load_csv(df: pd.DataFrame, path: str) -> None:
    logger = get_run_logger()
    df.to_csv(path, index=False)
    logger.info("📤 Saved %d rows to %s", len(df), path)

@task
def validate_business_logic(df: pd.DataFrame, tax_rate: float = 1.2, atol: float = 1e-6) -> pd.DataFrame:
    logger = get_run_logger()
    recomputed = (df['Revenue'] * tax_rate).round(2)
    mismatch = (df['Revenue_with_Tax'] - recomputed).abs() > atol
    if mismatch.any():
        bad_idx = df.index[mismatch].tolist()[:5]
        raise ValueError(f"Business rule mismatch for rows (showing up to 5): {bad_idx}")
    logger.info("✅ Business rule check passed: Revenue_with_Tax == Revenue * tax_rate")
    return df

# ----------------------
# Flow
# ----------------------
@flow(name="Prefect ETL with Data Validation")
def etl_with_validation(
    input_path: str = "data/source_data.csv",
    output_path: str = "data/final_data.csv",
    required_columns: List[str] = ["Month", "Revenue"],
    numeric_nonneg_cols: List[str] = ["Revenue"],
    tax_rate: float = 1.2
):
    # Extract
    df = extract_csv(input_path)

    # Validate (pre-transform)
    df = validate_required_columns(df, required_columns)
    df = validate_rowcount(df, min_rows=1)
    df = validate_no_nulls(df, [c for c in required_columns if c != 'Month'])
    df = validate_numeric_nonnegative(df, numeric_nonneg_cols)

    # Transform
    df = transform_add_tax(df, tax_rate=tax_rate)

    # Validate (post-transform)
    df = validate_required_columns(df, required_columns + ["Revenue_with_Tax"])
    df = validate_business_logic(df, tax_rate=tax_rate)

    # Load
    load_csv(df, output_path)

if __name__ == "__main__":
    # Example run (make sure data/source_data.csv exists)
    etl_with_validation()
