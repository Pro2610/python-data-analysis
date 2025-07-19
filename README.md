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

## 🧪 Sample Output

```python
Original:
     Name     Age     JoinDate
0   Alice      25    2022-01-10
1     Bob  thirty    2022/02/15
2   Clara      35    15-03-2022
3    None      40          None

Cleaned:
    Name   Age   JoinDate
0  alice  25.0 2022-01-10
2  clara  35.0 2022-03-15
