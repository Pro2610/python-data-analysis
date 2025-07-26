# 📊 Streamlit Sales Dashboard — Explanation

This app demonstrates how to build an **interactive dashboard** using Streamlit.

---

1. 🛠 Simulate Sales Data

We generate synthetic data for demonstration:

```python
np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
categories = ['Electronics', 'Clothing', 'Home']

data = pd.DataFrame({
    'Month': np.random.choice(months, 100),
    'Category': np.random.choice(categories, 100),
    'Sales': np.random.randint(100, 1000, 100)
})
2. 🎨 Create Streamlit UI
st.title() adds a title

st.write() adds description text

st.selectbox() creates a dropdown filter for category

3. 📈 KPI Metrics
We calculate Total Sales and Average Sales:

python
Copiar
Editar
total_sales = data['Sales'].sum()
avg_sales = data['Sales'].mean()
Then display with Streamlit metrics:

python
Copiar
Editar
col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Average Sales", f"${avg_sales:,.0f}")
4. 📋 Data Table
Use st.dataframe(data) to show the filtered dataset interactively.

5. 📊 Sales Trend Chart
Group data by month and plot:

python
Copiar
Editar
sales_by_month = data.groupby('Month')['Sales'].sum().reindex(months)
plt.plot(sales_by_month.index, sales_by_month.values, marker='o')
st.pyplot(fig)
✅ Why Streamlit?
No HTML/CSS required

Instant UI for Python scripts

Easy deployment to web
