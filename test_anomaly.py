from anomaly import make_transactions, detect
def test_recall():
    df, true_idx = make_transactions(n=500, seed=7)
    pred, _ = detect(df, contamination=0.04)
    import numpy as np
    flagged = set(np.where(pred == -1)[0])
    recall = len(flagged & true_idx) / len(true_idx)
    assert recall >= 0.5, f"recall too low {recall}"
    assert len(flagged) <= 40
def test_api_shape():
    from fastapi.testclient import TestClient
    from app import app
    c = TestClient(app)
    r = c.post("/score", json={"amount": 500.0, "hour": 2})
    assert r.status_code == 200
    assert "anomaly" in r.json()
