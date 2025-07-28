import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 1. App Config
# ---------------------------
st.set_page_config(page_title="Advanced Sales Dashboard", layout="wide")

# ---------------------------
# 2. Sidebar Navigation
# ---------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Dashboard", "Upload Data"])

# ---------------------------
# 3. Load Data (Simulated or Uploaded)
# ---------------------------
@st.cache_data
def load_default_data():
    np.random.seed(42)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    categories = ['Electronics', 'Clothing', 'Home']
    data = pd.DataFrame({
        'Month': np.random.choice(months, 100),
        'Category': np.random.choice(categories, 100),
        'Sales': np.random.randint(100, 1000, 100)
    })
    return data

if page == "Home":
    st.title("📊 Advanced Streamlit Dashboard")
    st.write("This app demonstrates a multi-page dashboard with interactive features.")
    st.write("Use the sidebar to navigate between pages.")

elif page == "Upload Data":
    st.title("📂 Upload Your Own Dataset")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.success("Data loaded successfully!")
        st.write(data.head())
    else:
        st.info("Upload a CSV file to see the preview.")

elif page == "Dashboard":
    st.title("📈 Sales Dashboard")

    # Load default data
    data = load_default_data()

    # Sidebar filter
    categories = list(data['Category'].unique())
    selected_category = st.sidebar.selectbox("Filter by Category:", ["All"] + categories)
    if selected_category != "All":
        data = data[data['Category'] == selected_category]

    # KPIs
    total_sales = data['Sales'].sum()
    avg_sales = data['Sales'].mean()
    transactions = data.shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${total_sales:,.0f}")
    col2.metric("Average Sales", f"${avg_sales:,.0f}")
    col3.metric("Transactions", transactions)

    # Charts
    st.subheader("Sales by Month")
    sales_by_month = data.groupby('Month')['Sales'].sum()
    fig1, ax1 = plt.subplots()
    ax1.plot(sales_by_month.index, sales_by_month.values, marker='o')
    ax1.set_title('Sales Trend')
    st.pyplot(fig1)

    st.subheader("Sales by Category")
    sales_by_category = data.groupby('Category')['Sales'].sum()
    fig2, ax2 = plt.subplots()
    ax2.bar(sales_by_category.index, sales_by_category.values, color=['blue','orange','green'])
    st.pyplot(fig2)

    st.subheader("Category Distribution (Pie)")
    fig3, ax3 = plt.subplots()
    ax3.pie(sales_by_category.values, labels=sales_by_category.index, autopct='%1.0f%%', startangle=90)
    ax3.axis('equal')
    st.pyplot(fig3)
