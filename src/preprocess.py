import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from .config import FEATURE_COLUMNS, TIMESTAMP_COL

def load_and_scale(path: Path):
    """Read CSV or Excel, drop NaNs, sort by timestamp, return scaled array."""
    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)

    df.columns = [c.strip() for c in df.columns]   # trim whitespace
    df = df.dropna(subset=FEATURE_COLUMNS).sort_values(TIMESTAMP_COL)

    raw_features = df[FEATURE_COLUMNS].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(raw_features)

    return df, X_scaled
