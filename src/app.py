import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="AI E-Commerce Dashboard",
    layout="wide"
)

# --------------------------------
# LOAD DATA
# --------------------------------

df = pd.read_csv(
    "data/raw/Superstore_sales.csv",
    encoding="latin1"
)

# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.title("Filters")

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

# --------------------------------
# FILTER DATA
# --------------------------------

filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter))
]

# --------------------------------
# TITLE
# --------------------------------

st.title("AI E-Commerce Intelligence Dashboard")

st.markdown("---")

# --------------------------------
# KPIs
# --------------------------------

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
profit_margin = (
    total_profit / total_sales
) * 100

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)

st.markdown("---")

# --------------------------------
# REGION SALES CHART
# --------------------------------

region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region",
    title="Region Wise Sales"
)

# --------------------------------
# CATEGORY SALES
# --------------------------------

category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    category_sales,
    names="Category",
    values="Sales",
    title="Category Contribution"
)

# --------------------------------
# MONTHLY SALES TREND
# --------------------------------

filtered_df["Order_Date"] = pd.to_datetime(
    filtered_df["Order_Date"]
)

filtered_df["Month"] = (
    filtered_df["Order_Date"]
    .dt.month_name()
)

monthly_sales = (
    filtered_df
    .groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

fig3 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

# --------------------------------
# DISPLAY CHARTS
# --------------------------------

c1, c2 = st.columns(2)

with c1:
    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with c2:
    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# --------------------------------
# MACHINE LEARNING SECTION
# --------------------------------

st.subheader("AI Sales Prediction")

X = df[["Quantity", "Discount"]]
y = df["Sales"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

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

prediction = model.predict(
    [[quantity_input, discount_input]]
)

st.success(
    f"Predicted Sales: ${prediction[0]:,.2f}"
)

st.markdown("---")

# --------------------------------
# DATA PREVIEW
# --------------------------------

st.subheader("Dataset Preview")

st.dataframe(filtered_df.head(20))