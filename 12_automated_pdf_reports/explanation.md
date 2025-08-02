# 📄 Automated PDF Reports — Explanation

This script generates a **professional PDF report** that includes KPIs, a data table, and a chart.

---

## ✅ Key Steps:

### 1. **Generate Sample Data**
We create a dataset with monthly sales and compute:
- **Total Sales**
- **Average Sales**
```python
data = pd.DataFrame({'Month': ['Jan','Feb','Mar','Apr','May'], 'Sales': [1000,1500,1200,1700,2000]})
total_sales = data['Sales'].sum()
avg_sales = data['Sales'].mean()

2. Create Chart

A simple line chart is generated using matplotlib and saved as an image:

plt.plot(data['Month'], data['Sales'], marker='o')
plt.savefig('sales_chart.png')

3. Generate PDF with FPDF

Add title and date

Insert KPIs (Total Sales, Average Sales)

Create a table from the dataset

Add the chart image to the PDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Sales Report', ln=True, align='C')

4. Save PDF

The final report is saved as:

sales_report.pdf

✅ Result: A clean PDF with:

Title and date

KPIs

Data table

Chart

⚠ Tip:

You can extend this script to:

Add multiple charts

Format tables better

Generate multi-page reports
