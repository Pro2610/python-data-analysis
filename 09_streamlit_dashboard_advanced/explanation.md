# 📊 Advanced Streamlit Dashboard — Explanation

This app demonstrates a **multi-page dashboard** using Streamlit with interactive features and charts.

---

## ✅ Key Components:

### 1. **App Configuration**
```python
st.set_page_config(page_title="Advanced Sales Dashboard", layout="wide")

Sets title and wide layout for a better dashboard experience.

2. Sidebar Navigation

We created multiple pages:

Home: Introduction

Upload Data: Allows users to upload their own CSV

Dashboard: Shows charts and KPIs

page = st.sidebar.radio("Go to:", ["Home", "Dashboard", "Upload Data"])

3. Data Handling

By default, we generate synthetic data.

Users can upload their own dataset on the "Upload Data" page.

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

4. Filters

We use selectbox for category filtering:

selected_category = st.sidebar.selectbox("Filter by Category:", ["All"] + categories)

5. KPIs

We calculate and display key metrics:

Total Sales

Average Sales

Transactions count

Displayed using:

col1.metric("Total Sales", f"${total_sales:,.0f}")

6. Charts

Line Chart: Sales by month

Bar Chart: Sales by category

Pie Chart: Category distribution

All rendered with matplotlib and st.pyplot(fig).

✅ Why This Dashboard?

Multi-page navigation improves usability

Dynamic KPIs and filters allow interactive analysis

Upload feature makes it practical for real data

