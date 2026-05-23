import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI E-Commerce Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = pd.read_csv(
    "data/raw/Superstore_sales.csv",
    encoding='latin1'
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.markdown("""
# 📊 AI E-Commerce Intelligence Dashboard

### Real-Time Business Insights & Sales Forecasting
""")

st.markdown("---")

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
profit_margin = (total_profit / total_sales) * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Total Sales",
        f"${total_sales:,.2f}"
    )

with col2:
    st.metric(
        "📈 Total Profit",
        f"${total_profit:,.2f}"
    )

with col3:
    st.metric(
        "🔥 Profit Margin",
        f"{profit_margin:.2f}%"
    )

st.markdown("---")

# ---------------------------------------------------
# REGION WISE SALES
# ---------------------------------------------------

st.subheader("📍 Region Wise Sales")

region_sales = df.groupby("Region")["Sales"].sum()

st.bar_chart(region_sales)

# ---------------------------------------------------
# CATEGORY CONTRIBUTION
# ---------------------------------------------------

st.subheader("🛒 Category Contribution")

category_sales = df.groupby("Category")["Sales"].sum()

fig, ax = plt.subplots(figsize=(5, 5))

ax.pie(
    category_sales,
    labels=category_sales.index,
    autopct='%1.1f%%'
)

st.pyplot(fig)

# ---------------------------------------------------
# MONTHLY SALES TREND
# ---------------------------------------------------

st.subheader("📈 Monthly Sales Trend")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = df.groupby(
    df["Order_Date"].dt.month
)["Sales"].sum()

fig2, ax2 = plt.subplots(figsize=(10, 4))

ax2.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o'
)

ax2.set_xlabel("Month")
ax2.set_ylabel("Sales")
ax2.set_title("Monthly Sales Trend")

st.pyplot(fig2)

# ---------------------------------------------------
# AI SALES PREDICTION SECTION
# ---------------------------------------------------

st.markdown("---")

st.subheader("🤖 AI Sales Prediction")

quantity_input = st.slider(
    "Select Quantity",
    1,
    20,
    5
)

discount_input = st.slider(
    "Select Discount",
    0.0,
    1.0,
    0.2
)

predicted_sales = (
    quantity_input * 120
) - (discount_input * 100)

st.success(
    f"Predicted Sales: ${predicted_sales:.2f}"
)

# ---------------------------------------------------
# DATA PREVIEW
# ---------------------------------------------------

st.markdown("---")

st.subheader("📄 Dataset Preview")

st.dataframe(df.head())