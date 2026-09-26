from fastapi import FastAPI
from pydantic import BaseModel
from anomaly import detect
import pandas as pd
app = FastAPI(title="Stripe-style Anomaly API - Charan Teja")
class Txn(BaseModel):
    amount: float
    hour: int
@app.get("/")
def root(): return {"status": "ok"}
@app.post("/score")
def score(t: Txn):
    import numpy as np
    df = pd.DataFrame([{"amount": t.amount, "hour": t.hour}] * 10)
    pred, scores = detect(df, contamination=0.1)
    return {"anomaly": bool(pred[0] == -1), "score": float(scores[0])}
