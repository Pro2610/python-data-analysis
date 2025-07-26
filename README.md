# 🧹 01 — Data Cleaning in Python

This module covers essential techniques for cleaning and preparing data using Python and `pandas`.

Cleaning data is a fundamental step in the data analysis process — it ensures data quality, consistency, and usability before visualization or modeling.

---

## 🧠 Covered Topics

- Handling missing values
- Cleaning text fields (e.g., trim, lowercase)
- Type conversions (numeric, date)
- Filtering out invalid entries
- Basic pandas usage

---

## 📁 Files

| File                      | Description                                  |
|---------------------------|----------------------------------------------|
| `task.md`                | Description of the cleaning task             |
| `cleaning_examples.ipynb`| Code examples for common cleaning steps      |
| `explanation.md`         | Step-by-step explanation of logic and output |

---



# 📊 02 — Data Visualization in Python
This module shows how to use pandas, matplotlib, and seaborn to create simple but powerful visualizations for business analytics.

✅ Covered Topics:

Bar charts for revenue analysis

Line charts to track user growth

Pie charts for segment distribution

Heatmaps to analyze correlations

🔧 Libraries Used:

pandas — for data manipulation

matplotlib.pyplot — for plotting

seaborn — for advanced visuals (heatmaps, style)

📁 Files:

| File                          | Description                                  |
|-------------------------------|----------------------------------------------|
| `task.md`                     | Task description for this module             |
| `visualization_examples.ipynb`| Jupyter Notebook with 4 chart examples       |
| `explanation.md`              | Commentary and logic behind each graph       |
 

📌 Example Use Case:

📈 Monthly Active Users over time (Line Chart) helps track engagement trends.

🔥 Correlation Matrix (Heatmap) can help reveal which variables are related.

---

# 🔍 03 — Exploratory Data Analysis (EDA)
This module demonstrates the most important first steps in understanding your dataset using Python.

✅ Covered Topics:

Dataset overview (shape, info, describe)

Missing values and duplicates detection

Distribution analysis using histograms

Outlier detection with boxplots

Feature comparison using groupby

🔧 Libraries Used:

pandas — data manipulation

matplotlib.pyplot — basic plotting

seaborn — advanced visuals (boxplot)

📁 Files:	   

| File                          | Description                                  |
|-------------------------------|----------------------------------------------|
| `task.md`                     |  Task overview                               |
| `eda_examples.ipynb`          |  Code notebook with EDA steps                |
| `explanation.md`              | Explanation of each technique used           |


📌 Example Use Cases:

🧩 Quickly identify columns with missing or invalid values.

📦 Detect outliers in salary or age using boxplots.

# 🧽 04 Advanced Data Cleaning
This module demonstrates advanced techniques for cleaning messy and inconsistent datasets using Python and pandas.

✅ Covered Topics:

Normalizing categorical data (e.g., .str.strip().lower())

Validating email formats using regex

Parsing inconsistent date formats

Removing outliers using simple rules

Handling duplicates with custom logic

Imputing missing values (mean)

🔧 Libraries Used:

pandas

numpy

re (for regular expressions)

🧮 Analyze group-wise metrics like average salary per department.

---

📁 Files:	   

| File                          | Description                                  |
|-------------------------------|----------------------------------------------|
| `task.md`                     |  Task overview                               |
| `cleaning_advanced_04.ipynb`  |  Code examples                               |
| `explanation.md`              | Explanation of each method used              |


📌 Example Use Cases:

💡 Standardize customer names and emails for deduplication

🧹 Prepare messy survey or CRM exports before analysis

# 🛠 05 Feature Engineering in Python
This module demonstrates how to create new features and transform existing ones for better analysis and modeling.

✅ Covered Topics:

Extracting date components (year, month, weekday)

One-hot encoding for categorical variables

Binning continuous variables

Log transformations to reduce skewness

Scaling numeric features using:

StandardScaler (mean=0, std=1)

MinMaxScaler (range [0,1])

🔧 Libraries Used:

pandas

numpy

sklearn.preprocessing

📁 Files:

| File                          | Description                                  |
|-------------------------------|----------------------------------------------|
| `task.md`                     | Overview of feature engineering objectives   |
| `feature_engineering.ipynb`   | Notebook with step-by-step examples          |
| `explanation.md`              | Explanation of each technique                |


📌 Example Use Cases:

📅 Extract time-based features for seasonality analysis

🔤 Encode categories for machine learning models

📈 Normalize and scale numeric features for better performance in ML algorithms

# 🧪 06 A/B Testing Simulation in Python
This module demonstrates how to simulate and analyze an A/B test using Python, calculate statistical significance, and visualize the results.

✅ Covered Topics:

Generating synthetic data for control (A) and test (B) groups

Calculating key metrics:

Conversion Rate

ARPU (Average Revenue Per User)

Performing Z-test for proportions

Visualizing results with bar charts

Interpreting statistical results and making business decisions

🔧 Libraries Used:

pandas

numpy

matplotlib

scipy.stats

📁 Files:

| File                          | Description                                                        |
|-------------------------------|--------------------------------------------------------------------|
| `task.md`                     | Overview of the A/B testing simulation                             |
| `ab_testing.ipynb`            | Jupyter Notebook with data simulation, analysis, and visualization |
| `explanation.md`              | Explanation of the process and interpretation                      |

📌 Example Insights:

✅ If p-value < 0.05, the Test group performs significantly better than the Control group.
✅ Always analyze both conversion rate and revenue for business impact.

# 📑 07 Data Reporting in Python
This module demonstrates how to create automated Excel and PDF reports from data analysis using Python.

✅ Covered Topics:

Creating summary tables and visualizations

Exporting data and metrics to Excel (multiple sheets)

Generating PDF reports with:

Text elements

Embedded charts

Automating reporting workflows

🔧 Libraries Used:

pandas — for data manipulation and Excel export

matplotlib — for plotting charts

openpyxl — for Excel formatting

reportlab — for generating PDFs

📁 Files:

| File                          | Description                                          |              
|-------------------------------|------------------------------------------------------|
| `task.md`                     | Overview of the reporting task                       |
| `data_reporting.ipynb`        | Notebook with code to generate Excel and PDF reports |
| `explanation.md`              | Step-by-step explanation of each process             |

📌 Example Use Cases:

✅ Monthly business reports for management
✅ Automated KPI dashboards exported to Excel and PDF
✅ Marketing performance summaries with charts

# 📊 08 Streamlit Sales Dashboard
This module demonstrates how to build an interactive dashboard in Python using Streamlit for sales analysis.

✅ Features:

Interactive category filter (selectbox)

KPI metrics:

Total Sales

Average Sales

Dynamic data table

Sales trend visualization (line chart)

🔧 Libraries Used:

streamlit — for building the dashboard

pandas — for data manipulation

matplotlib — for visualization

numpy — for synthetic data generation

📁 Files:

| File                          | Description                                       |              
|-------------------------------|---------------------------------------------------|
| `task.md`                     | Overview of the dashboard task                    |
| `dashboard_app.py`            | Streamlit app code                                |
| `explanation.md`              | Explanation of each component in the app          |

▶️ How to Run:

Install dependencies:

pip install streamlit pandas matplotlib numpy

Run the app:

streamlit run dashboard_app.py

📌 Why Use Streamlit?

Fast prototyping for data apps

Interactive filters and charts without HTML/CSS

Ideal for sharing insights with teams


