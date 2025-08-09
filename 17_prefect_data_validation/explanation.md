# 📘 explanation.md
```markdown
# 🧠 Explanation — Prefect ETL with Data Validation

This flow demonstrates robust ETL with Prefect 2.0:

## Tasks
- `extract_csv(path)`: reads input CSV and logs row count.
- `validate_required_columns(df, required)`: ensures schema presence.
- `validate_rowcount(df)`: prevents empty loads.
- `validate_no_nulls(df, cols)`: blocks nulls in critical fields.
- `validate_numeric_nonnegative(df, cols)`: enforces numeric types and non-negativity.
- `transform_add_tax(df, tax_rate)`: adds `Revenue_with_Tax` (rounded to 2 decimals).
- `validate_business_logic(df, tax_rate)`: recomputes expected values and compares.
- `load_csv(df, path)`: writes final dataset.

## Flow
`etl_with_validation(...)` orchestrates all tasks in order:
Extract → Pre-validation → Transform → Post-validation → Load.

## Why Prefect?
- Clear task/flow separation
- Logging & visibility
- Easy to parameterize (paths, tax_rate)
- Ready for scheduling / deployments
