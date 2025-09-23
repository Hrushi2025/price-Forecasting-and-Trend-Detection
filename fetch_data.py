import yfinance as yf
import ccxt
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

assets = {
    "gold": "GC=F",
    "silver": "SI=F",
    "BTC_USDT": "BTC-USD",
    "ETH_USDT": "ETH-USD",
    "USD": "USD=X"
}

def download_save(name, ticker):
    try:
        df = yf.download(ticker, period="2y", interval="1h")
        df.to_csv(f"{name}.csv")
        print(f"{name}.csv saved with {len(df)} rows")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

with ThreadPoolExecutor(max_workers=5) as executor:
    for name, ticker in assets.items():
        executor.submit(download_save, name, ticker)



def fetch_gold_silver():
    gold = yf.download("GC=F", start="2023-01-01", end="2025-09-20", interval="1h")
    silver = yf.download("SI=F", start="2023-01-01", end="2025-09-20", interval="1h")
    return gold, silver

def fetch_fiat():
    usd = yf.download("USD=X", start="2023-01-01", end="2025-09-20", interval="1h")
    eur = yf.download("EUR=X", start="2023-01-01", end="2025-09-20", interval="1h")
    aed = yf.download("AED=X", start="2023-01-01", end="2025-09-20", interval="1h")
    return usd, eur, aed

def fetch_crypto():
    exchange = ccxt.binance()
    symbols = ['BTC/USDT', 'ETH/USDT']
    data = {}
    for symbol in symbols:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1h', since=exchange.parse8601('2023-01-01T00:00:00Z'))
        df = pd.DataFrame(ohlcv, columns=['timestamp','open','high','low','close','volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        data[symbol] = df
    return data

if __name__ == "__main__":
    gold, silver = fetch_gold_silver()
    usd, eur, aed = fetch_fiat()
    crypto_data = fetch_crypto()

    # Save locally
    gold.to_csv("gold.csv")
    silver.to_csv("silver.csv")
    usd.to_csv("usd.csv")
    eur.to_csv("eur.csv")
    aed.to_csv("aed.csv")
    for k, v in crypto_data.items():
        v.to_csv(f"{k.replace('/','_')}.csv")
