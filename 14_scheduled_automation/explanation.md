# ⏰ Scheduled Automation — Explanation

This script schedules the **automatic execution** of the previous block's report generation and email sending script.

---

## ✅ Key Steps:

### 1. **Define Job Function**
We define a function that calls the previous script (`pdf_email_report.py`) using `subprocess`:
```python
def run_report():
    subprocess.run(['python', 'pdf_email_report.py'])

2. Schedule the Job

Using the schedule library:

Option 1: Run every 10 minutes (for testing)

schedule.every(10).minutes.do(run_report)

Option 2: Run daily at a specific time (e.g., 09:00)

schedule.every().day.at("09:00").do(run_report)

3. Keep Script Running

An infinite loop checks for pending jobs every 60 seconds:

while True:

    schedule.run_pending()
    time.sleep(60)

✅ Why Use This Approach?

Simple Python-based scheduling (no extra tools needed)

Easy for local automation or server-based scripts

🔍 Bonus:

For production environments, consider:

Cron jobs (Linux)

Task Scheduler (Windows)

Airflow (advanced orchestration)
