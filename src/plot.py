import matplotlib.pyplot as plt
from pathlib import Path
from .config import FEATURE_COLUMNS, TIMESTAMP_COL

def plot_signals(df, preds, out_dir: Path):
    df = df.copy()
    df["is_anomaly"] = preds < 0

    fig, axes = plt.subplots(len(FEATURE_COLUMNS), 1,
                             figsize=(10, 7), sharex=True)
    fig.suptitle("Telemetry trends (red = potential anomaly)")

    for i, col in enumerate(FEATURE_COLUMNS):
        axes[i].plot(df[TIMESTAMP_COL], df[col], linewidth=1)
        axes[i].scatter(
            df.loc[df.is_anomaly, TIMESTAMP_COL],
            df.loc[df.is_anomaly, col],
            color="red", s=15, zorder=3,
            label="Anomaly" if i == 0 else None,
        )
        axes[i].set_ylabel(col)

    axes[-1].set_xlabel("Time")
    axes[0].legend()
    out_dir.mkdir(parents=True, exist_ok=True)
    img = out_dir / "telemetry_with_anomalies.png"
    plt.tight_layout()
    plt.savefig(img, dpi=150)
    plt.close(fig)
    return img
