import pandas as pd

def detect_anomalies(file):
    """
    Detects spikes and dips in forecasted values and saves anomalies to a new CSV.
    """
    # Read the forecast CSV
    df = pd.read_csv(file, index_col=0, parse_dates=True)

    # Compute mean and standard deviation of the predicted values
    mean = df['yhat'].mean()
    std = df['yhat'].std()

    # Detect spikes and dips
    df['spike'] = df['yhat'] > mean + 2 * std
    df['dip'] = df['yhat'] < mean - 2 * std

    # Save anomalies to a new file
    anomalies_file = file.replace(".csv", "_anomalies.csv")
    df.to_csv(anomalies_file)
    print(f"Anomalies saved: {anomalies_file}")

if __name__ == "__main__":
    # List all your forecast CSV files here
    files = [
        "gold_features_1h_forecast.csv",
        "gold_features_1d_forecast.csv",
        "gold_features_1w_forecast.csv",
        "gold_features_30d_forecast.csv",
        "silver_features_1h_forecast.csv",
        "silver_features_1d_forecast.csv",
        "silver_features_1w_forecast.csv",
        "silver_features_30d_forecast.csv",
        "BTC_USDT_features_1h_forecast.csv",
        "BTC_USDT_features_1d_forecast.csv",
        "BTC_USDT_features_1w_forecast.csv",
        "BTC_USDT_features_30d_forecast.csv",
        "ETH_USDT_features_1h_forecast.csv",
        "ETH_USDT_features_1d_forecast.csv",
        "ETH_USDT_features_1w_forecast.csv",
        "ETH_USDT_features_30d_forecast.csv"
    ]

    # Run anomaly detection for each file
    for f in files:
        detect_anomalies(f)
