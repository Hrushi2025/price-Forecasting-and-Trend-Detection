Price-Forecasting-and-Trend-Detection

---

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/a0b013d9-324f-48b5-bea6-a3e9caaa8f7f" />

---

Project Overview

---

This project is a comprehensive end-to-end financial analytics pipeline that:

Fetches historical market data for commodities, cryptocurrencies, and fiat currencies.

Cleans and preprocesses the data for analysis.

Generates technical features like returns, rolling mean, and volatility.

Trains Prophet models to forecast asset prices at multiple horizons (1-hour, 1-day, 1-week, 30-day).

Detects anomalies (spikes and dips) in forecasted prices.

Provides a structured folder-based workflow for organized storage of data, features, models, forecasts, and anomalies.

Can be extended to trigger real-time alerts and expose predictions via an API.

---

Project Workflow
Step	Description
1. Setup environment	Install Python 3.x and required libraries (yfinance, ccxt, pandas, prophet, joblib, matplotlib).
2. Fetch data	Download historical data for gold, silver, BTC, ETH, USD, EUR, AED.
3. Explore & clean data	Handle missing values, standardize timestamps, ensure proper columns (close) exist.
4. Feature engineering	Calculate returns, rolling_mean_3, rolling_std_3 for each asset.
5. Train model	Train Prophet models on feature-engineered data for each asset.
6. Forecast prices	Generate predictions for multiple horizons: 1-hour, 1-day, 1-week, 30-day.
7. Detect anomalies	Identify spikes and dips using statistical thresholds (mean ± 2σ).
8. Trigger alerts (optional)	Send notifications (email/SMS) when anomalies or thresholds are detected.
9. Build API (optional)	Expose predictions and anomalies for a frontend dashboard.
10. Visualize	Generate plots for historical trends, rolling statistics, forecasts, and detected anomalies.

---

Folder Structure:

---


<img width="2048" height="2048" alt="image" src="https://github.com/user-attachments/assets/7e9cef04-b1ed-4be7-9f8f-11ecebcf3805" />

---


Libraries Required

pandas – Data manipulation and feature engineering

yfinance – Historical price data for commodities, fiat, and crypto

ccxt – Cryptocurrency data from exchanges like Binance

prophet – Forecasting time series data

joblib – Saving and loading trained models

matplotlib – Plotting price trends and forecasts

---

Install via pip:

pip install pandas yfinance ccxt prophet joblib matplotlib

Usage Instructions
1. Data Download
python download_data.py

---

Downloads all required assets and saves in raw_data/.

2. Data Cleaning
python clean_data.py

---

Cleans raw CSVs and saves cleaned files in output/.

3. Feature Engineering
python features.py

---

Adds returns, rolling_mean_3, rolling_std_3.

Saves feature CSVs in features_output/.

4. Train Prophet Models
python train_prophet.py

---

Trains models for each asset and saves in models_output/.

5. Forecast Prices
python forecast.py

---

Generates forecasts for 1h, 1d, 1w, 30d and saves CSVs in forecast_output/.

6. Detect Anomalies
python anomalies.py

---

Detects spikes and dips in forecasts.

Saves anomalies in anomalies_output/.

Anomaly Detection Logic

Spikes: forecasted price > mean + 2 * standard deviation

Dips: forecasted price < mean - 2 * standard deviation

Anomalies can trigger alerts in future integration (email, SMS, webhook).

---

Visualizations

Historical price trends

Rolling mean and volatility

Forecasted values for multiple horizons

Highlighted spikes (red) and dips (green) in anomalies

---

Extensibility

Integrate ARIMA or LSTM models for advanced forecasting.

Real-time streaming of crypto/forex data.

API for serving forecasts and anomalies.

Dashboard integration using Streamlit or Dash.
 
---

Conclusion

This project provides a modular, scalable, and organized pipeline for financial data analysis, forecasting, and anomaly detection. Each step produces outputs in dedicated folders for clean management and reproducibility. It is suitable for research, trading insights, and further AI-driven financial applications.
