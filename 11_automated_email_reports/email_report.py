import smtplib
import pandas as pd
import matplotlib.pyplot as plt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl

# ---------------------------
# 1. Generate Sample Report
# ---------------------------
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [1000, 1500, 1200, 1700, 2000]
})

total_sales = data['Sales'].sum()
avg_sales = data['Sales'].mean()

# ---------------------------
# 2. Create Chart
# ---------------------------
plt.figure(figsize=(6,4))
plt.plot(data['Month'], data['Sales'], marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
chart_file = 'sales_chart.png'
plt.savefig(chart_file)
plt.close()

# ---------------------------
# 3. Email Configuration
# ---------------------------
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_app_password"  # Use app password for Gmail

subject = "Automated Sales Report"
body = f"""
<h2>Sales Report</h2>
<p><b>Total Sales:</b> ${total_sales:,.0f}</p>
<p><b>Average Sales:</b> ${avg_sales:,.0f}</p>
<p>See attached chart for details.</p>
"""

# ---------------------------
# 4. Compose Email
# ---------------------------
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'html'))

# Attach image
with open(chart_file, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={chart_file}')
    msg.attach(part)

# ---------------------------
# 5. Send Email via SMTP
# ---------------------------
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email sent successfully!")
