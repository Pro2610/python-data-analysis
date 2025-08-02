from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
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
# 3. Generate PDF with FPDF
# ---------------------------
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Sales Report', ln=True, align='C')

# Date
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f'Date: {datetime.now().strftime("%Y-%m-%d")}', ln=True, align='C')
pdf.ln(10)

# KPIs
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, f'Total Sales: ${total_sales:,.0f}', ln=True)
pdf.cell(0, 10, f'Average Sales: ${avg_sales:,.0f}', ln=True)
pdf.ln(10)

# Table Header
pdf.set_font('Arial', 'B', 12)
pdf.cell(40, 10, 'Month', 1)
pdf.cell(50, 10, 'Sales', 1)
pdf.ln()

# Table Rows
pdf.set_font('Arial', '', 12)
for i, row in data.iterrows():
    pdf.cell(40, 10, row['Month'], 1)
    pdf.cell(50, 10, f"${row['Sales']}", 1)
    pdf.ln()

# Insert Chart
pdf.ln(10)
pdf.image(chart_file, x=10, w=180)

# Save PDF
output_file = 'sales_report.pdf'
pdf.output(output_file)

print(f"✅ PDF report generated: {output_file}")
