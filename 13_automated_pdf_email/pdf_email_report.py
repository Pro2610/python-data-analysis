import smtplib
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
from datetime import datetime

# ---------------------------
# 1. Generate Sample Data
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
# 3. Generate PDF Report
# ---------------------------
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Sales Report', ln=True, align='C')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f'Date: {datetime.now().strftime("%Y-%m-%d")}', ln=True, align='C')
pdf.ln(10)
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, f'Total Sales: ${total_sales:,.0f}', ln=True)
pdf.cell(0, 10, f'Average Sales: ${avg_sales:,.0f}', ln=True)
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(40, 10, 'Month', 1)
pdf.cell(50, 10, 'Sales', 1)
pdf.ln()
pdf.set_font('Arial', '', 12)
for _, row in data.iterrows():
    pdf.cell(40, 10, row['Month'], 1)
    pdf.cell(50, 10, f"${row['Sales']}", 1)
    pdf.ln()
pdf.ln(10)
pdf.image(chart_file, x=10, w=180)
pdf_file = 'sales_report.pdf'
pdf.output(pdf_file)

# ---------------------------
# 4. Configure Email
# ---------------------------
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_app_password"  # Use Gmail App Password

subject = "Automated Sales Report"
body = f"""
<h2>Sales Report</h2>
<p><b>Total Sales:</b> ${total_sales:,.0f}</p>
<p><b>Average Sales:</b> ${avg_sales:,.0f}</p>
<p>Full report attached as PDF.</p>
"""

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'html'))

# Attach PDF
with open(pdf_file, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={pdf_file}')
    msg.attach(part)

# ---------------------------
# 5. Send Email via SMTP
# ---------------------------
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email with PDF report sent successfully!")
