# 🏙️ Smart City Assistant

A real-time, AI-powered assistant designed to help city citizens and authorities make better decisions using urban data, predictive intelligence, and natural language understanding.

## 🚀 Project Overview

Smart City Assistant is an interactive agentic system that synthesizes multimodal city data, generates insights using LLMs, and offers predictive alerts. The goal is to empower urban decision-making for smarter, safer, and more sustainable cities.

## 🌟 Features

- 🔍 **AI Assistant**: Built using Google Gemini/IBM Granite for contextual understanding.
- 📊 **Real-Time Data Integration**: Processes live inputs like traffic, weather, and pollution.
- 🗺️ **Dashboard**: Interactive Streamlit interface for visualizing data and insights.
- 📡 **Alerts & Recommendations**: Proactive suggestions based on predictive analytics.
- 🔐 **Firebase Backend**: Authentication and database integration.
- 🌐 **Location-aware Agent**: Responses customized based on user's area/locality.

## 🧠 Tech Stack

| Technology     | Role                        |
|----------------|-----------------------------|
| Python         | Backend processing & logic  |
| Streamlit      | Frontend dashboard UI       |
| Google Gemini / IBM Granite | Language Model integration |
| Firebase       | Database + Auth             |
| Google Maps API| Location data integration   |
| Pinecone       | Semantic vector search (if used) |

## 🛠️ How to Run

```bash
# Step 1: Clone the Repository
git clone https://github.com/Lachi9959/smart_city_assistant.git
cd smart_city_assistant

# Step 2: Install Dependencies
pip install -r requirements.txt

# Step 3: Set up Firebase config and API keys
# Create .env file and add your credentials

# Step 4: Run the Streamlit App
streamlit run app.py
