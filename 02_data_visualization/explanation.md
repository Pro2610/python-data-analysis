# 📘 Data Visualization — Explanation

This notebook demonstrates how to use pandas, matplotlib, and seaborn for basic visualizations.

---

## 1. 📊 Bar Chart — Revenue by Category

**What it shows:**  
Revenue values for different product categories.

**Why it's useful:**  
Clear comparison between categories, useful in financial or product performance dashboards.

```python
revenue_data.plot(kind='bar', x='Category', y='Revenue')

2. 📈 Line Chart — Monthly Active Users
What it shows:
User growth (or drop) across time, month by month.

Why it's useful:
Ideal for tracking trends like MAU, DAU, retention, etc.

python
Copiar
Editar
plt.plot(maus['Month'], maus['Users'], marker='o')

3. 🥧 Pie Chart — User Segments
What it shows:
Share of each user type in the user base.

Why it's useful:
Visual representation of user segmentation. Use with caution — pie charts are best with few, clearly separated categories.

python
Copiar
Editar
segments.plot(kind='pie', autopct='%1.0f%%')

4. 🔥 Heatmap — Correlation Matrix
What it shows:
Correlation between numerical variables (from -1 to 1)

Why it's useful:
Helps detect multicollinearity, or find predictive relationships.

python
Copiar
Editar
sns.heatmap(corr, annot=True, cmap='coolwarm')

