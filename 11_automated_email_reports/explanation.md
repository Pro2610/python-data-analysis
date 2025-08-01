# 📧 Automated Email Reports — Explanation

This script automates the process of generating a data report and sending it via email with an attachment.

---

## ✅ Key Steps:

### 1. **Generate Sample Report**

We create a small dataset with sales by month and calculate summary metrics:
```python
data = pd.DataFrame({'Month': ['Jan','Feb','Mar','Apr','May'], 'Sales': [1000,1500,1200,1700,2000]})
total_sales = data['Sales'].sum()
avg_sales = data['Sales'].mean()

2. Create Chart

We visualize the data with matplotlib and save it as sales_chart.png:

plt.plot(data['Month'], data['Sales'], marker='o')
plt.savefig('sales_chart.png')
3. Configure Email
SMTP: Uses Gmail SMTP server (smtp.gmail.com)

Authentication: Requires App Password for security

Define sender, recipient, subject, and email body (HTML):

sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_app_password"

4. Compose Email with Attachment

Attach the chart as a file using email.mime modules:

msg.attach(MIMEText(body, 'html'))

5. Send via SMTP

Using SSL for secure connection:

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

✅ Result: The recipient receives an email with a summary (HTML body) and an attached chart image.

⚠ Security Note:

Use an App Password for Gmail, not your main password.
