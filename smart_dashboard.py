import streamlit as st
from reports.report_generator import generate_sustainability_report
import pandas as pd

st.set_page_config(page_title="Smart City Dashboard", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<h1 class="title">🌆 Smart City Assistant Dashboard</h1>', unsafe_allow_html=True)

prompt = st.text_input("Ask a question to the assistant")
if st.button("Submit"):
    from app.llm.granite_llm import ask_granite
    st.success(ask_granite(prompt))

if st.button("Show Forecast"):
    from ml.kpi_file_forecaster import forecast_kpi
    forecast_kpi("water_usage.csv")
    st.image("forecast_plot.png")

if st.button("Show Anomalies"):
    from ml.anomaly_file_checker import detect_anomalies
    df = detect_anomalies("water_usage.csv")
    st.dataframe(df)

if st.button("Generate Report"):
    report = generate_sustainability_report(300, 450, "2025-06-30", 2)
    st.markdown(report)
    st.download_button("Download as .md", report, file_name="report.md")
