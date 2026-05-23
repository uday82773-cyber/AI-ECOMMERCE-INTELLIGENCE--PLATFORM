import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("🔍 Filter Dashboard")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

# Apply Filters

df = df[
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter))
]

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
# CHART SECTION
# ---------------------------------------------------

col_chart1, col_chart2 = st.columns(2)

# REGION SALES CHART

with col_chart1:

    st.subheader("📍 Region Wise Sales")

    region_sales = df.groupby("Region")["Sales"].sum()

    fig = px.bar(
        x=region_sales.index,
        y=region_sales.values,
        color=region_sales.index,
        title="Region Wise Sales Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# CATEGORY PIE CHART

with col_chart2:

    st.subheader("🛒 Category Contribution")

    category_sales = df.groupby("Category")["Sales"].sum()

    fig2 = px.pie(
        values=category_sales.values,
        names=category_sales.index,
        title="Category Contribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ---------------------------------------------------
# MONTHLY SALES TREND
# ---------------------------------------------------

st.markdown("---")

st.subheader("📈 Monthly Sales Trend")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = df.groupby(
    df["Order_Date"].dt.month
)["Sales"].sum()

fig3, ax3 = plt.subplots(figsize=(12, 4))

ax3.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o'
)

ax3.set_xlabel("Month")
ax3.set_ylabel("Sales")
ax3.set_title("Monthly Sales Trend")

st.pyplot(fig3)

# ---------------------------------------------------
# AI SALES PREDICTION
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
# DATASET PREVIEW
# ---------------------------------------------------

st.markdown("---")

st.subheader("📄 Dataset Preview")

st.dataframe(df.head())