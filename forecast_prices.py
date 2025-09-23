import pandas as pd
import joblib
from prophet import Prophet
import os

files = ["gold_features.csv", "silver_features.csv", "BTC_USDT_features.csv", "ETH_USDT_features.csv"]
forecast_periods = {
    "1h": 1,
    "1d": 24,
    "1w": 24*7,
    "30d": 24*30
}

def forecast_prices(file):
    # Load feature CSV
    df = pd.read_csv(file, index_col=0, parse_dates=True)
    df_prophet = df.reset_index()[['close']]
    df_prophet.rename(columns={'index':'ds', 'close':'y'}, inplace=True)

    # Load trained model
    model_file = file.replace(".csv","") + "_prophet_model.pkl"
    model = joblib.load(model_file)

    for period_name, period_hours in forecast_periods.items():
        future = model.make_future_dataframe(periods=period_hours, freq='H')
        forecast = model.predict(future)
        forecast_file = file.replace(".csv","") + f"_{period_name}_forecast.csv"
        forecast.to_csv(forecast_file)
        print(f"Forecast saved: {forecast_file}")

for f in files:
    try:
        forecast_prices(f)
    except Exception as e:
        print(f"Error forecasting {f}: {e}")
