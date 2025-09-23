import pandas as pd
import matplotlib.pyplot as plt
import os

# Folder where your CSVs are stored
data_folder = "."
files = ["gold.csv", "silver.csv", "BTC_USDT.csv", "ETH_USDT.csv", "USD.csv", "EUR.csv", "AED.csv"]

def clean_data(file):
    df = pd.read_csv(file)

    # Detect datetime column
    datetime_cols = [c for c in df.columns if "date" in c.lower() or "timestamp" in c.lower()]
    if datetime_cols:
        datetime_col = datetime_cols[0]
        df[datetime_col] = pd.to_datetime(df[datetime_col], errors='coerce')
        df = df.dropna(subset=[datetime_col])
        df.set_index(datetime_col, inplace=True)
    else:
        # fallback: first column as datetime
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

    # Fill missing values
    df = df.ffill().bfill()
    return df

def plot_data(df, title):
    plt.figure(figsize=(10,4))
    plt.plot(df['close'], label='Close Price')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

# Process all files
for f in files:
    path = os.path.join(data_folder, f)
    try:
        df = clean_data(path)
        print(f"{f} cleaned. {len(df)} rows available.")
        plot_data(df, f"Price Trend: {f.split('.')[0]}")
        # Save cleaned CSV for next step
        df.to_csv(f.replace(".csv", "_cleaned.csv"))
    except Exception as e:
        print(f"Error processing {f}: {e}")
