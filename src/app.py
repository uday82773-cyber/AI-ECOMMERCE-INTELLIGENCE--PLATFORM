import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/raw/Superstore_sales.csv",encoding='latin1')

# Title
st.title("AI E-Commerce Intelligence Dashboard")

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Total Profit", f"${total_profit:,.2f}")

# Region wise sales
st.subheader("Region Wise Sales")

region_sales = df.groupby("Region")["Sales"].sum()

st.bar_chart(region_sales)