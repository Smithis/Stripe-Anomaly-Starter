import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

def make_transactions(n=1000, seed=7):
    rng = np.random.default_rng(seed)
    normal = rng.normal(loc=100.0, scale=20.0, size=n)
    # inject 20 fraud-like spikes
    idx = rng.choice(n, size=20, replace=False)
    normal[idx] = rng.normal(loc=400.0, scale=50.0, size=20)
    df = pd.DataFrame({"amount": normal, "hour": rng.integers(0, 24, size=n)})
    return df, set(idx)

def detect(df, contamination=0.02):
    X = df[["amount", "hour"]].values
    clf = IsolationForest(contamination=contamination, random_state=7)
    pred = clf.fit_predict(X)  # -1 anomaly
    scores = -clf.score_samples(X)
    return pred, scores

if __name__ == "__main__":
    df, true_idx = make_transactions()
    pred, scores = detect(df)
    flagged = set(np.where(pred == -1)[0])
    recall = len(flagged & true_idx) / max(len(true_idx), 1)
    print(f"flagged={len(flagged)} recall={recall:.2f} mean_score={scores.mean():.3f}")
