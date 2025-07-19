# 🧠 Data Cleaning — Explanation

This example includes:

### 1. Strip and lowercase text
Helps standardize names (e.g., ' Alice ' → 'alice')

### 2. Type conversion
- `pd.to_numeric()` for numeric fields
- `pd.to_datetime()` to handle dates with different formats

### 3. Handling errors
- `errors='coerce'` replaces invalid values with NaN

### 4. Removing missing/invalid entries
- `dropna()` used to remove rows missing any of the key fields
