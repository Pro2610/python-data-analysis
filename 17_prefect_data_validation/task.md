# ✅ Prefect — ETL with Data Validation

## Goal
Build a Prefect 2.0 flow that performs ETL with **data quality checks**.

## Steps
1. **Extract** CSV data
2. **Validate (pre-transform)**:
   - required columns present
   - non-empty dataset
   - no nulls in numeric fields
   - numeric & non-negative checks
3. **Transform**: add `Revenue_with_Tax = Revenue * tax_rate`
4. **Validate (post-transform)**:
   - business rule: `Revenue_with_Tax == Revenue * tax_rate`
5. **Load** cleaned data to CSV

## Run
```bash
pip install prefect pandas
python prefect_data_validation.py
