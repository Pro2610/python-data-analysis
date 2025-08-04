# 📧 Automated PDF Report + Email Integration — Explanation

This script combines **PDF report generation** with **email automation**, allowing you to create and send professional reports automatically.

---

## ✅ Key Steps:

### 1. **Generate Sample Data**
We create a dataset with monthly sales and compute:
- Total Sales
- Average Sales
```python
data = pd.DataFrame({'Month': ['Jan','Feb','Mar','Apr','May'], 'Sales': [1000,1500,1200,1700,2000]})
2. Create Chart
A line chart of monthly sales using matplotlib:

plt.plot(data['Month'], data['Sales'], marker='o')
plt.savefig('sales_chart.png')

3. Generate PDF with FPDF

Add title and date

Insert KPIs (Total & Average Sales)

Build data table

Insert chart image

Save as sales_report.pdf

4. Compose Email

Using email.mime to:

Set HTML body with KPIs

Attach the PDF report

5. Send Email via SMTP

Secure connection using smtplib and ssl:

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

✅ Result: Recipient gets an email with:

HTML summary (KPIs)

Attached PDF report

⚠ Security Note:

Use Gmail App Password instead of your real password.
