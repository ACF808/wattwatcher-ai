import argparse
from pathlib import Path
from datetime import datetime
import pandas as pd
from .preprocess import load_and_scale
from .model import train_iforest
from .plot import plot_signals
from .config import FEATURE_COLUMNS, TIMESTAMP_COL

# --- simple suggestion rules ------------------------------------------
def suggest_fix(row):
    cur, volt, rpm = row[FEATURE_COLUMNS].values
    mean_cur, mean_volt, mean_rpm = row.means
    tips = []
    if cur > 1.5 * mean_cur and rpm < 0.8 * mean_rpm:
        tips.append("Check for mechanical jam / overload.")
    if volt < 0.9 * mean_volt:
        tips.append("Inspect power wiring or battery health.")
    if not tips:
        tips.append("Investigate sensor noise or unusual load.")
    return "; ".join(tips)

# ----------------------------------------------------------------------
def main(path):
    data_path = Path(path)
    df, X_scaled = load_and_scale(data_path)

    preds, scores = train_iforest(X_scaled)

    # quick means for rule-of-thumb suggestions
    means = df[FEATURE_COLUMNS].mean()
    df["means"] = [means] * len(df)

    df["anomaly_score"] = scores
    df["is_anomaly"]    = preds < 0
    df.loc[df.is_anomaly, "suggestion"] = (
        df[df.is_anomaly]
        .apply(suggest_fix, axis=1)
    )

    # ------------------------------------------------------------------
    #  Create a unique run folder: outputs/<timestamp>_runN
    # ------------------------------------------------------------------
    from datetime import datetime
    base_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    root    = Path("outputs")
    root.mkdir(exist_ok=True)

    # increment run number if folder already exists
    run_num = 1
    while True:
        out_dir = root / f"{base_ts}_run{run_num}"
        try:
            out_dir.mkdir()
            break                   # success
        except FileExistsError:
            run_num += 1            # try the next number

    # ------------------------------------------------------------------
    #  Save full report + suggestions-only report
    # ------------------------------------------------------------------
    full_report = out_dir / "anomaly_report.csv"
    df.to_csv(full_report, index=False)

    sugg_rows = df[df["is_anomaly"] == True]
    if not sugg_rows.empty:
        keep = [TIMESTAMP_COL, *FEATURE_COLUMNS, "anomaly_score", "suggestion"]
        sugg_rows.to_csv(out_dir / "suggestions_only.csv",
                         columns=keep, index=False)

    # ------------------------------------------------------------------
    #  Plot
    # ------------------------------------------------------------------
    plot_path = plot_signals(df, preds, out_dir)
  
    # ------------------------------------------------------------------
    #  Console summary
    # ------------------------------------------------------------------
    print(f"\nOutputs folder : {out_dir}")
    print(f"  • Full report       : {full_report.name}")
    if not sugg_rows.empty:
        print(f"  • Suggestions only  : suggestions_only.csv")
    print(f"  • Trend plot        : {plot_path.name}")
    print(f"\nAnomalies found : {df.is_anomaly.sum()}\n")
    print("⚠️  DISCLAIMER: Suggestions are AI-generated for educational",
          "purposes only and are NOT an official electrical diagnosis.\n")


# ------------------ KEEP THIS AT LEFT EDGE ------------------
if __name__ == "__main__":
    import argparse, pathlib
    parser = argparse.ArgumentParser(description="AI motor/electrical diagnostics")
    parser.add_argument("--file", required=True, help="Path to CSV or Excel file")
    args = parser.parse_args()
    main(args.file)
# ------------------------------------------------------------