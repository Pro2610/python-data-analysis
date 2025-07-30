import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

st.set_page_config(page_title="A/B Test Analyzer", layout="wide")

# ---------------------------
# 1. Title & Description
# ---------------------------
st.title("🧪 A/B Test Analyzer")
st.write("Upload an A/B test dataset and analyze results (Conversion Rate, ARPU, Significance).")

# ---------------------------
# 2. Upload CSV
# ---------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(data.head())

    # Validate required columns
    required_cols = {'group', 'converted', 'revenue'}
    if not required_cols.issubset(data.columns):
        st.error(f"CSV must contain columns: {required_cols}")
    else:
        # ---------------------------
        # 3. Compute Metrics
        # ---------------------------
        metrics = data.groupby('group').agg(
            users=('converted', 'count'),
            conversions=('converted', 'sum'),
            conversion_rate=('converted', 'mean'),
            arpu=('revenue', 'mean')
        )

        st.subheader("📊 Metrics Summary")
        st.dataframe(metrics)

        # ---------------------------
        # 4. Statistical Test (Z-test)
        # ---------------------------
        if 'A' in metrics.index and 'B' in metrics.index:
            a_conv = metrics.loc['A', 'conversions']
            b_conv = metrics.loc['B', 'conversions']
            n_A = metrics.loc['A', 'users']
            n_B = metrics.loc['B', 'users']

            p_A = a_conv / n_A
            p_B = b_conv / n_B
            p_pool = (a_conv + b_conv) / (n_A + n_B)
            se = np.sqrt(p_pool * (1 - p_pool) * (1/n_A + 1/n_B))

            z_score = (p_B - p_A) / se
            p_value = 1 - stats.norm.cdf(z_score)

            st.subheader("📐 Z-test Result")
            st.write(f"Z-score: {z_score:.2f}")
            st.write(f"P-value: {p_value:.4f}")
            if p_value < 0.05:
                st.success("✅ Significant difference: Test group outperforms Control.")
            else:
                st.info("⚠ No significant difference detected.")

        # ---------------------------
        # 5. Charts
        # ---------------------------
        st.subheader("📈 Conversion Rate by Group")
        fig1, ax1 = plt.subplots()
        ax1.bar(metrics.index, metrics['conversion_rate'], color=['skyblue', 'lightgreen'])
        ax1.set_ylabel('Conversion Rate')
        st.pyplot(fig1)

        st.subheader("📈 ARPU by Group")
        fig2, ax2 = plt.subplots()
        ax2.bar(metrics.index, metrics['arpu'], color=['orange', 'green'])
        ax2.set_ylabel('ARPU')
        st.pyplot(fig2)
else:
    st.info("Please upload a CSV file to start analysis.")
