# 📘 Exploratory Data Analysis — Explanation

This notebook covers the core steps of EDA using a small mock dataset.

---

## 1. 📄 Load and Preview Data

We start by creating a sample dataset using `pandas.DataFrame`. This allows us to test various EDA techniques.

```python
data.head()

## 2. ℹ️ Basic Info & Statistics
.shape shows the size of the dataset.
.info() reveals data types and nulls.
.describe() gives summary statistics like mean, std, min, max, etc.

## 3. 🧩 Missing Values
We check for missing values using:

python
Copiar
Editar
data.isnull().sum()
This helps us understand data quality and where imputation might be needed.

## 4. 🔁 Duplicates
To avoid biased results, we check for duplicated rows:

python
Copiar
Editar
data.duplicated().sum()

##5. 📊 Histograms
Histograms help analyze distributions of numerical variables (e.g., age, salary).

python
Copiar
Editar
data.hist()
This is useful to detect skewness and outliers.

##6. 📦 Boxplots
Boxplots show median, quartiles, and outliers in a single view.
We used seaborn.boxplot() to explore salary distribution.

##7. 🧮 Grouped Analysis
With .groupby(), we calculate the mean salary per department. This is useful for comparisons across categories.

python
Copiar
Editar
data.groupby('department')['salary'].mean()

