import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from analysis import (
    load_data,
    get_live_weather,
    get_live_aqi,
    calculate_correlations,
    lag_analysis,
    weather_significance
)

st.set_page_config(
    page_title="Urban Air Intelligence",
    layout="wide"
)

st.title("🌍 Urban Air Intelligence Dashboard")

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("Settings")

city = st.sidebar.text_input(
    "Enter City",
    "Mysuru"
)

# -----------------------------
# Live Data Section
# -----------------------------

st.header("📡 Real-Time Environmental Data")

aqi_data = get_live_aqi(city)
weather_data = get_live_weather(city)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("AQI", aqi_data["AQI"])

with col2:
    st.metric("PM2.5", aqi_data["PM25"])

with col3:
    st.metric("Temperature °C", weather_data["Temperature"])

with col4:
    st.metric("Wind Speed km/h", weather_data["WindSpeed"])

# -----------------------------
# Upload Dataset
# -----------------------------

st.header("📂 Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # -----------------------------
    # Correlation Analysis
    # -----------------------------

    st.header("📊 Correlation Analysis")

    results = calculate_correlations(df)

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Pearson Correlation",
            round(results["pearson"], 3)
        )

    with c2:
        st.metric(
            "Spearman Correlation",
            round(results["spearman"], 3)
        )

    st.write(
        f"P-Value: {results['pvalue']:.5f}"
    )

    # -----------------------------
    # Lag Analysis
    # -----------------------------

    st.header("⏳ Lag Analysis")

    lag_results = lag_analysis(df)

    st.write(
        f"1 Hour Lag Correlation: {lag_results['lag1']:.3f}"
    )

    st.write(
        f"2 Hour Lag Correlation: {lag_results['lag2']:.3f}"
    )

    # -----------------------------
    # Weather Significance
    # -----------------------------

    st.header("🌦 Weather Impact Analysis")

    weather_corr, weather_p = weather_significance(df)

    st.write(
        f"Wind Speed Correlation: {weather_corr:.3f}"
    )

    st.write(
        f"P-Value: {weather_p:.5f}"
    )

    # -----------------------------
    # Heatmap
    # -----------------------------

    st.header("🔥 Correlation Matrix")

    numeric_df = df.select_dtypes(
        include="number"
    )

    corr_matrix = numeric_df.corr()

    fig, ax = plt.subplots(
        figsize=(8, 6)
    )

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

    # -----------------------------
    # Bivariate Analysis
    # -----------------------------

    st.header("📈 Bivariate Analysis")

    columns = [
        "PM2.5_Level",
        "NO2_Level",
        "Traffic_Volume_Count",
        "Wind_Speed_kmh",
        "Temperature_C"
    ]

    x_var = st.selectbox(
        "Select X Variable",
        columns
    )

    y_var = st.selectbox(
        "Select Y Variable",
        columns,
        index=1
    )

    fig2, ax2 = plt.subplots()

    sns.regplot(
        x=df[x_var],
        y=df[y_var],
        ax=ax2
    )

    ax2.set_xlabel(x_var)
    ax2.set_ylabel(y_var)

    st.pyplot(fig2)
