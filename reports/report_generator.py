from app.llm.granite_llm import ask_granite

def generate_sustainability_report(avg_water, avg_energy, peak_date, anomaly_count):
    prompt = f"""
You are a sustainability assistant. Based on:
- Avg Water: {avg_water} L
- Avg Energy: {avg_energy} kWh
- Peak Date: {peak_date}
- Anomalies: {anomaly_count}
Generate a report with:
1. Summary
2. Trends
3. Suggestions
4. Conclusion
"""
    return ask_granite(prompt)
