# 🛠 Feature Engineering — Explanation

This notebook demonstrates how to create and transform features for better analysis and modeling.

---

## 1. 📅 Extract Date Features

We used `dt` accessors to extract **year**, **month**, and **weekday** from a date column:

```python
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['weekday'] = data['date'].dt.day_name()
