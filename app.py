import streamlit as st

st.set_page_config(
    page_title="Project FORESIGHT",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Project FORESIGHT")
st.subheader("AI-Powered Demand and Inventory Intelligence Platform")

st.divider()

st.header("📌 Overview")

st.write(
    "Project FORESIGHT is an AI-powered demand and inventory "
    "intelligence platform that provides:"
)

st.markdown("""
- 📈 Demand Forecasting & Prediction
- 📦 Inventory Intelligence & Optimization
- ⚠️ Inventory Risk Scoring & Alerts
- 🌦️ Seasonality & Demand Pattern Analysis
- 📊 Business Intelligence Dashboard
""")

st.divider()

st.header("🧠 System Architecture")

st.write(
    "Data → Processing → Feature Engineering → "
    "ML Models → Forecasting → Risk Scoring → "
    "Dashboard → Insights"
)

st.success("✅ System is running successfully")

st.info("👉 Use sidebar to navigate between modules")