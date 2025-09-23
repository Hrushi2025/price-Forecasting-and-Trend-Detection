import pandas as pd
from prophet import Prophet
import joblib

def clean_csv_for_prophet(file):
    """
    Reads CSV robustly and prepares dataframe for Prophet
    """
    df = pd.read_csv(file)

    # Detect datetime column
    datetime_cols = [c for c in df.columns if "date" in c.lower() or "timestamp" in c.lower()]
    if datetime_cols:
        datetime_col = datetime_cols[0]
        df[datetime_col] = pd.to_datetime(df[datetime_col], errors='coerce')
        df = df.dropna(subset=[datetime_col])
        df.set_index(datetime_col, inplace=True)
    else:
        # fallback: use first column as datetime
        df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], errors='coerce')
        df = df.dropna(subset=[df.columns[0]])
        df.set_index(df.columns[0], inplace=True)

    # Ensure 'close' column exists
    if 'close' not in df.columns:
        if 'Close' in df.columns:
            df['close'] = df['Close']
        elif 'Adj Close' in df.columns:
            df['close'] = df['Adj Close']
        else:
            raise ValueError(f"No close column found in {file}")

    # Prepare for Prophet
    df_prophet = df.reset_index()[[df.index.name, 'close']].rename(columns={df.index.name: 'ds', 'close': 'y'})
    return df_prophet

if __name__ == "__main__":
    files = ["gold_features.csv", "silver_features.csv", "BTC_USDT_features.csv", "ETH_USDT_features.csv"]

    for f in files:
        try:
            df_prophet = clean_csv_for_prophet(f)
            model = Prophet(daily_seasonality=True, weekly_seasonality=True)
            model.fit(df_prophet)
            model_file = f.replace(".csv","") + "_prophet_model.pkl"
            joblib.dump(model, model_file)
            print(f"Model trained and saved as {model_file}")
        except Exception as e:
            print(f"Error training {f}: {e}")
