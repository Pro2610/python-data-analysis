# 🧪 A/B Testing Simulation — Explanation

This notebook demonstrates the steps for running and analyzing an A/B test using Python.

---

## 1. 🎲 Generate Synthetic Data

We created two groups:
- **A (Control)**: baseline experience
- **B (Test)**: variant experience

Steps:
- Simulated conversions with `np.random.binomial`
- Assigned revenue only to converted users using `np.random.normal`

---

## 2. 📊 Calculate Metrics

Grouped by `group` and computed:
- `users`: total users in each group
- `conversions`: number of converted users
- `conversion_rate`: conversions / users
- `arpu`: average revenue per user

---

## 3. ✅ Statistical Test (Z-test)

Hypotheses:
- **H₀**: Conversion rates are equal
- **H₁**: Conversion rate of B > A

Z-score and p-value calculation:
- `p_pool` = combined conversion rate
- `SE` = standard error
- If `p-value < 0.05`, reject H₀ → significant difference

---

## 4. 📈 Visualization

Two bar charts:
- Conversion Rate comparison
- ARPU comparison

Helps visually confirm which group performs better.

---

### 🧠 Key Insight:
A/B testing ensures that improvements in metrics are statistically significant, not due to random chance.
