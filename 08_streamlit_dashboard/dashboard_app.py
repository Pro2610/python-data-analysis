import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 1. Simulate Sales Data
# ---------------------------
np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
categories = ['Electronics', 'Clothing', 'Home']

data = pd.DataFrame({
    'Month': np.random.choice(months, 100),
    'Category': np.random.choice(categories, 100),
    'Sales': np.random.randint(100, 1000, 100)
})

# ---------------------------
# 2. Streamlit Dashboard
# ---------------------------
st.title("📊 Sales Dashboard")
st.write("Interactive dashboard for analyzing monthly sales data.")

# Filter by Category
selected_category = st.selectbox("Select Category:", ['All'] + categories)

if selected_category != 'All':
    data = data[data['Category'] == selected_category]

# ---------------------------
# 3. KPI Metrics
# ---------------------------
total_sales = data['Sales'].sum()
avg_sales = data['Sales'].mean()

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Average Sales", f"${avg_sales:,.0f}")

# ---------------------------
# 4. Data Table
# ---------------------------
st.subheader("Sales Data")
st.dataframe(data)

# ---------------------------
# 5. Line Chart (Sales by Month)
# ---------------------------
sales_by_month = data.groupby('Month')['Sales'].sum().reindex(months)
fig, ax = plt.subplots()
ax.plot(sales_by_month.index, sales_by_month.values, marker='o')
ax.set_title('Sales by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
st.pyplot(fig)
