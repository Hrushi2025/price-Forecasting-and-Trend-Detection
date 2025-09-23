import pandas as pd
import os

files = ["gold_cleaned.csv", "silver_cleaned.csv", "BTC_USDT_cleaned.csv", "ETH_USDT_cleaned.csv",
         "USD_cleaned.csv", "EUR_cleaned.csv", "AED_cleaned.csv"]

def add_features(df):
    # Ensure 'close' is numeric
    df['close'] = pd.to_numeric(df['close'], errors='coerce')

    # Drop rows where 'close' is NaN after conversion
    df = df.dropna(subset=['close'])

    # Returns
    df['returns'] = df['close'].pct_change()

    # Rolling mean / volatility
    df['rolling_mean_3'] = df['close'].rolling(window=3).mean()
    df['rolling_std_3'] = df['close'].rolling(window=3).std()

    return df

# Process all files
for f in files:
    try:
        df = pd.read_csv(f, index_col=0, parse_dates=True)

        # Apply feature engineering
        df = add_features(df)

        # Save feature file
        feature_file = f.replace("_cleaned.csv", "_features.csv")
        df.to_csv(feature_file)
        print(f"{feature_file} saved with {len(df)} rows")
    except Exception as e:
        print(f"Error processing {f}: {e}")
