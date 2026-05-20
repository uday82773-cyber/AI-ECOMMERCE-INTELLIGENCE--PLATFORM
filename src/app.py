import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AI E-Commerce Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv("data/raw/Superstore_sales.csv", encoding='latin1')

# ----------------------------
# TITLE
# ----------------------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #333;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)
    
st.markdown("---")

# ----------------------------
# SIDEBAR FILTERS
# ----------------------------
st.sidebar.header("Filters")

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

# Filter Data
filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter))
]

# ----------------------------
# KPI SECTION
# ----------------------------
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
profit_margin = (total_profit / total_sales) * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Sales", f"${total_sales:,.2f}")

with col2:
    st.metric("📈 Total Profit", f"${total_profit:,.2f}")

with col3:
    st.metric("📊 Profit Margin", f"{profit_margin:.2f}%")

st.markdown("---")

# ----------------------------
# REGION WISE SALES
# ----------------------------
region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region",
    title="Region Wise Sales"
)
fig_region.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig_region, use_container_width=True)

# ----------------------------
# CATEGORY WISE SALES
# ----------------------------
category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig_category = px.pie(
    category_sales,
    names="Category",
    values="Sales",
    title="Category Wise Sales"
)
fig_category.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig_category, use_container_width=True)

# ----------------------------
# MONTHLY SALES TREND
# ----------------------------
filtered_df["Order_Date"] = pd.to_datetime(filtered_df["Order_Date"],errors="coerce")
monthly_sales = (
    filtered_df.groupby(filtered_df["Order_Date"].dt.month)["Sales"]
    .sum()
    .reset_index()
)

monthly_sales.columns = ["Month", "Sales"]

fig_month = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)
fig_month.update_layout(
    template="plotly_dark",
    height=500
)
st.plotly_chart(fig_month, use_container_width=True)

# ----------------------------
# DATA PREVIEW
# ----------------------------
st.subheader("Dataset Preview")

st.dataframe(filtered_df.head())