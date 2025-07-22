# 📘 Advanced Data Cleaning — Explanation

This document explains the logic behind each step in `cleaning_advanced.ipynb`.

---

## 1. 🧩 Sample Data

We created a sample `pandas` DataFrame with common data issues:
- Extra spaces and inconsistent case in text
- Invalid or missing emails
- Inconsistent date formats
- Outliers and null values in numeric columns

---

## 2. 🔤 Normalize Categorical Text

We cleaned the `name` column by removing extra spaces and converting all names to lowercase using:

```python
.str.strip().str.lower()

## 3. 📧 Validate Email Format
Using a regular expression (regex), we checked if the email matches a standard pattern:

python
Copiar
Editar
str.contains(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$')
This flags malformed or missing emails.

## 4. 🕒 Parse Date Strings
The join_date column contains multiple date formats. We used:

python
Copiar
Editar
pd.to_datetime(..., errors='coerce')
to convert all to consistent datetime format and mark unparseable values as NaT.

## 5. 📦 Outlier Removal
To catch invalid ages (e.g., negative or over 120), we used a conditional rule with apply() and np.nan.

## 6. 🔁 Custom Duplicate Removal
Duplicates were handled using normalized lowercase names. We dropped duplicates by:

python
Copiar
Editar
drop_duplicates(subset=['name_lower'])

## 7. 💸 Impute Missing Income
Missing income values were filled with the column mean:

python
Copiar
Editar
fillna(data['income'].mean())
This preserves dataset size while reducing bias from nulls.

