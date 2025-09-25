#Basic configuration
FEATURE_COLUMNS = ["Current", "Voltage", "speed_rpm"]   # ← use these exact names
TIMESTAMP_COL   = "Date"                                # ← already matches

ANOMALY_CONTAMINATION = 0.05      # ~5 % of points can be flagged
RANDOM_SEED = 42

