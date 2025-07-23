# 🛠 Feature Engineering — Explanation

This notebook demonstrates how to create and transform features for better analysis and modeling.

---

## 1. 📅 Extract Date Features

We used `dt` accessors to extract **year**, **month**, and **weekday** from a date column:

```python
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['weekday'] = data['date'].dt.day_name()

This is useful for seasonal trend analysis.

##2. 🔤 One-Hot Encoding

Convert categorical variables into dummy/indicator variables:

python
Copiar
Editar
pd.get_dummies(data, columns=['category', 'weekday'], drop_first=True)
drop_first=True avoids multicollinearity.

## 3. 🧱 Binning

Group continuous variables into intervals:

python
Copiar
Editar
pd.cut(data['sales'], bins=[0,150,300,500], labels=['Low','Medium','High'])
Helps in simplifying data and reducing noise.

## 4. 🔍 Log Transformation

Reduce skewness in numeric variables:

python
Copiar
Editar
np.log1p(data['sales'])
log1p handles zeros safely.

## 5. 📏 Scaling Features

Standardize and normalize features for modeling:

python
Copiar
Editar
StandardScaler()  # mean=0, std=1
MinMaxScaler()    # scales to [0,1]
This ensures fair comparison between features with different units.

