# 🚀 Prefect Deployments & Scheduling

## Goal
Turn your Prefect flow into a **deployment** with parameters and a **daily schedule**.

## What you'll do
1. Use the existing flow `etl_with_validation` from `prefect_data_validation.py`
2. Build a **deployment** with a name and work queue
3. Add a **cron schedule** (e.g., every day at 09:00)
4. Pass **parameters** (e.g., different input/output paths, tax_rate)

## Prereqs
- `prefect_data_validation.py` from the previous module available in the same repo
- Prefect 2.x installed (`pip install prefect`)
- (Optional) Prefect Cloud or Prefect Server for UI

## Runbook (CLI)
```bash
# 1) Start an agent (in a separate terminal)
prefect agent start -q default

# 2) Build a deployment from your flow
prefect deployment build prefect_data_validation.py:etl_with_validation \
  -n daily-9am \
  -q default \
  --params '{"tax_rate": 1.2, "input_path": "data/source_data.csv", "output_path": "data/final_data.csv"}' \
  --cron "0 9 * * *" \
  -o 17_prefect_deployments/etl_with_validation-deployment.yaml

# 3) Apply the deployment
prefect deployment apply 17_prefect_deployments/etl_with_validation-deployment.yaml

# 4) Run now (manual trigger)
prefect deployment run 'etl_with_validation/daily-9am'
```
