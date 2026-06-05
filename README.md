# 🌍 Urban Air Intelligence Dashboard

## Overview

Urban Air Intelligence is a real-time environmental analytics dashboard that studies the relationship between:

- Air Quality (PM2.5, NO₂, AQI)
- Traffic Volume
- Weather Conditions

The dashboard combines live environmental data and historical datasets to help identify pollution patterns and understand the impact of traffic and weather on air quality.

---

## Features

### 📡 Real-Time Monitoring
- Live AQI data
- Live PM2.5 levels
- Live temperature data
- Live wind speed data

### 📊 Correlation Analysis
- Pearson Correlation
- Spearman Correlation
- Statistical significance testing (P-Value)

### ⏳ Lag Analysis
- 1-hour lag correlation
- 2-hour lag correlation
- Traffic impact analysis on air quality

### 🔥 Correlation Matrix
- Interactive heatmap of environmental variables

### 📈 Bivariate Analysis
- Compare any two environmental variables
- Trendline visualization
- Interactive variable selection

---

## Dataset

Expected CSV columns:

| Column |
|----------|
| Timestamp |
| PM2.5_Level |
| NO2_Level |
| Traffic_Volume_Count |
| Wind_Speed_kmh |
| Temperature_C |

---

## Technologies Used

- Python
- Streamlit
- Pandas
- SciPy
- Seaborn
- Matplotlib
- Requests API

---

## Project Structure

```text
urban-air-intelligence/
│
├── app.py
├── analysis.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd urban-air-intelligence
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## API Configuration

Add the following secrets in Streamlit Cloud:

```toml
OPENWEATHER_API_KEY = "your_openweather_api_key"
WAQI_TOKEN = "your_waqi_token"
```

---

## Deployment

Deploy using:

- GitHub
- Streamlit Community Cloud

---

## Problem Statement

Urban pollution is influenced by traffic congestion and weather conditions. Understanding these relationships helps cities improve environmental planning and pollution management.

---

## Solution

This dashboard provides:

- Real-time AQI monitoring
- Weather monitoring
- Traffic impact analysis
- Correlation studies
- Lag effect analysis
- Interactive visualizations

to support data-driven environmental decision making.

---

## Future Enhancements

- Live traffic API integration
- AQI forecasting
- City-wise comparison
- Automated alerts
- Predictive analytics

---

## Author

Hackathon Project – Urban Air Intelligence Dashboard
