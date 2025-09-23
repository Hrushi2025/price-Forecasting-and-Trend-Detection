import pandas as pd
import smtplib

def send_email_alert(subject, message, to_email):
    from_email = "hrushikeshpardeshi2025@gmail.com"
    password = "hrushi@2025"

    body = f"Subject: {subject}\n\n{message}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, body)

def check_alerts(file):
    df = pd.read_csv(file, index_col=0, parse_dates=True)
    for i, row in df.iterrows():
        if row.get('spike', False):
            send_email_alert("Price Spike Alert", f"Spike detected at {i} - {row['yhat']}", "receiver@gmail.com")
        if row.get('dip', False):
            send_email_alert("Price Dip Alert", f"Dip detected at {i} - {row['yhat']}", "receiver@gmail.com")

if __name__ == "__main__":
    # List all forecast files and map them to anomaly files
    forecast_files = [
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

    # Convert forecast files to anomaly files
    anomaly_files = [f.replace(".csv", "_anomalies.csv") for f in forecast_files]

    # Check alerts for each anomaly file
    for f in anomaly_files:
        check_alerts(f)
