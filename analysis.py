import pandas as pd
import requests
from scipy.stats import pearsonr, spearmanr
import streamlit as st


# -----------------------------
# Load Dataset
# -----------------------------

def load_data(file):

    df = pd.read_csv(file)

    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    return df


# -----------------------------
# Live Weather Data
# -----------------------------

def get_live_weather(city):

    api_key = st.secrets["OPENWEATHER_API_KEY"]

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    return {
        "Temperature": data["main"]["temp"],
        "WindSpeed": round(data["wind"]["speed"] * 3.6, 2)
    }


# -----------------------------
# Live AQI Data
# -----------------------------

def get_live_aqi(city):

    token = st.secrets["WAQI_TOKEN"]

    url = (
        f"https://api.waqi.info/feed/{city}/"
        f"?token={token}"
    )

    response = requests.get(url)
    data = response.json()

    aqi = data["data"]["aqi"]

    pm25 = None

    if "pm25" in data["data"]["iaqi"]:
        pm25 = data["data"]["iaqi"]["pm25"]["v"]

    return {
        "AQI": aqi,
        "PM25": pm25
    }


# -----------------------------
# Pearson + Spearman
# -----------------------------

def calculate_correlations(df):

    pearson_corr, pearson_p = pearsonr(
        df["Traffic_Volume_Count"],
        df["PM2.5_Level"]
    )

    spearman_corr, spearman_p = spearmanr(
        df["Traffic_Volume_Count"],
        df["PM2.5_Level"]
    )

    return {
        "pearson": pearson_corr,
        "spearman": spearman_corr,
        "pvalue": pearson_p
    }


# -----------------------------
# Lag Analysis
# -----------------------------

def lag_analysis(df):

    lag1 = (
        df["Traffic_Volume_Count"]
        .shift(1)
        .corr(df["PM2.5_Level"])
    )

    lag2 = (
        df["Traffic_Volume_Count"]
        .shift(2)
        .corr(df["PM2.5_Level"])
    )

    return {
        "lag1": lag1,
        "lag2": lag2
    }


# -----------------------------
# Weather Significance
# -----------------------------

def weather_significance(df):

    corr, p_value = pearsonr(
        df["Wind_Speed_kmh"],
        df["PM2.5_Level"]
    )

    return corr, p_value
