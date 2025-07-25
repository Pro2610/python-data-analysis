# 📑 Data Reporting — Explanation

This notebook demonstrates how to generate Excel and PDF reports from data analysis results using Python.

---

1. 🗂 Create Sample Data

We built a simple dataset:

```python
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [1000, 1500, 1200, 1700, 2000]
})
2. 📊 Generate Summary Table
Using pandas:

python
Copiar
Editar
summary = pd.DataFrame({
    'Total Sales': [data['Sales'].sum()],
    'Average Sales': [data['Sales'].mean()]
})
This gives us key metrics for the report.

3. 📈 Plot Sales Chart
A simple line chart of monthly sales using matplotlib:

python
Copiar
Editar
plt.plot(data['Month'], data['Sales'], marker='o')
plt.savefig('sales_chart.png')
Saved as an image for embedding in the PDF report.

4. 📄 Export to Excel
With pandas ExcelWriter:

python
Copiar
Editar
with pd.ExcelWriter('report.xlsx') as writer:
    data.to_excel(writer, sheet_name='Data')
    summary.to_excel(writer, sheet_name='Summary')
Creates an Excel file with two sheets: Data and Summary.

5. 🖨 Export to PDF
Using ReportLab to create a PDF report:

python
Copiar
Editar
from reportlab.pdfgen import canvas
c = canvas.Canvas('report.pdf')
c.drawString(100, 750, 'Sales Report')
c.drawImage('sales_chart.png', 100, 450)
c.save()
Adds:

Report title

Key metrics

Chart image

✅ Why it's useful?
Automates reporting process

Eliminates manual work in Excel

Ensures consistent formatting and branding
