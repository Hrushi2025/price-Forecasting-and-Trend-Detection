from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/forecast/{asset}")
def get_forecast(asset: str):
    file = f"{asset}_forecast.csv"
    df = pd.read_csv(file)
    return df.tail(10).to_dict(orient="records")  # return last 10 predictions

@app.get("/anomalies/{asset}")
def get_anomalies(asset: str):
    file = f"{asset}_anomalies.csv"
    df = pd.read_csv(file)
    return df[df['spike'] | df['dip']].tail(10).to_dict(orient="records")

# Run with: uvicorn 9_build_api:app --reload
