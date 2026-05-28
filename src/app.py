import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


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

from sklearn.ensemble import RandomForestRegressor

# Train Model

X = df[['Quantity', 'Discount']]
y = df['Sales']

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X, y)

# Prediction

prediction = rf_model.predict(
    [[quantity_input, discount_input]]
)

st.success(
    f"Predicted Sales: ${prediction[0]:,.2f}"
)

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest Model

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

# Predictions

rf_predictions = rf_model.predict(X_test)

# Metrics

rf_mae = mean_absolute_error(
    y_test,
    rf_predictions
)


st.markdown("---")

st.subheader("📊 Model Performance")

st.write(f"MAE Score: {rf_mae:.2f}")

r2 = r2_score(y_test, rf_predictions)

st.write(f"R2 Score: {r2:.2f}")



st.markdown("---")

st.subheader("📈 Feature Importance Analysis")

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

fig4, ax4 = plt.subplots(figsize=(8,4))

ax4.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

ax4.set_title("Feature Importance")
ax4.set_xlabel("Features")
ax4.set_ylabel("Importance Score")

st.pyplot(fig4)

st.download_button(
    label="📥 Download Dataset",
    data=df.to_csv(index=False),
    file_name="superstore_sales.csv",
    mime="text/csv"
)


# ---------------------------------------------------
# DATASET PREVIEW
# ---------------------------------------------------

st.markdown("---")

st.subheader("📈 Sales Forecast Trend")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Month"] = df["Order_Date"].dt.month

forecast_data = df.groupby("Month")["Sales"].sum().reset_index()

fig5, ax5 = plt.subplots(figsize=(10,4))

ax5.plot(
    forecast_data["Month"],
    forecast_data["Sales"],
    marker="o"
)

ax5.set_title("Monthly Forecast Trend")
ax5.set_xlabel("Month")
ax5.set_ylabel("Sales")

st.pyplot(fig5)

st.markdown("---")

st.subheader("📄 Dataset Preview")

st.dataframe(df.head())