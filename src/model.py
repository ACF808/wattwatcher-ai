from sklearn.ensemble import IsolationForest
from .config import ANOMALY_CONTAMINATION, RANDOM_SEED

def train_iforest(X_scaled):
    """Return Isolation-Forest predictions (−1/1) and anomaly scores."""
    clf = IsolationForest(
        contamination=ANOMALY_CONTAMINATION,
        n_estimators=200,
        random_state=RANDOM_SEED
    )
    clf.fit(X_scaled)
    preds  = clf.predict(X_scaled)           # −1 = anomaly, 1 = normal
    scores = -clf.decision_function(X_scaled)  # higher -> more anomalous
    return preds, scores

