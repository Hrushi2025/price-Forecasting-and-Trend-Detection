import pandas as pd
import matplotlib.pyplot as plt

def plot_forecast(file):
    # Forecast file
    df = pd.read_csv(file, index_col=0, parse_dates=True)

    # Corresponding anomalies file
    anomalies_file = file.replace(".csv", "_anomalies.csv")
    try:
        anomalies = pd.read_csv(anomalies_file, index_col=0, parse_dates=True)
    except FileNotFoundError:
        anomalies = None

    plt.figure(figsize=(12,6))

    # Plot normal trend (all points)
    plt.plot(df.index, df['yhat'], color='blue', label='Forecast')

    # Overlay spikes and dips if anomalies exist
    if anomalies is not None:
        if 'spike' in anomalies.columns:
            plt.scatter(anomalies.index[anomalies['spike']],
                        anomalies['yhat'][anomalies['spike']],
                        color='red', label='Spike', s=20)
        if 'dip' in anomalies.columns:
            plt.scatter(anomalies.index[anomalies['dip']],
                        anomalies['yhat'][anomalies['dip']],
                        color='green', label='Dip', s=20)

    plt.title(file)
    plt.xlabel("Time")
    plt.ylabel("Price / Forecast")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
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

    for f in files:
        plot_forecast(f)
