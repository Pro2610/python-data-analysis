import schedule
import time
import subprocess
from datetime import datetime

# ---------------------------
# 1. Define Job Function
# ---------------------------
def run_report():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running report...")
    # Call the previous script
    subprocess.run(['python', 'pdf_email_report.py'])
    print("✅ Report sent successfully!")

# ---------------------------
# 2. Schedule Options
# ---------------------------
# Option 1: Run every 10 minutes (for testing)
# schedule.every(10).minutes.do(run_report)

# Option 2: Run every day at 09:00
schedule.every().day.at("09:00").do(run_report)

print("⏳ Scheduler started. Waiting for next run...")

# ---------------------------
# 3. Keep Script Running
# ---------------------------
while True:
    schedule.run_pending()
    time.sleep(60)
