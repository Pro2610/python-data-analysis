# 🛠 Prefect 2.0 — ETL with Data Validation

A production-style ETL flow with **data quality checks** using Prefect 2.0.

## Features

- Pre-transform validations (schema, nulls, numeric)
- Business-rule validation after transform
- Parameterized `tax_rate`, input/output paths
- Clear logs via Prefect’s logger

## Project Files

- `prefect_data_validation.py` — main flow & tasks
- `task.md` — scope & steps
- `explanation.md` — detailed walkthrough

## Quickstart

```bash

pip install prefect pandas
python prefect_data_validation.py
Place input at data/source_data.csv:

Month,Revenue

Jan,1000
Feb,1500
Mar,1200
Apr,1700
May,2000
Jun,2100

Output: data/final_data.csv with Revenue_with_Tax.
