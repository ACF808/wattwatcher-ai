import streamlit as st
from pathlib import Path
import tempfile, os, io
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ------------ import your existing logic -------------------
from src.main import main as run_model          # analysis pipeline
# -----------------------------------------------------------

st.set_page_config(page_title="Motor Diagnostics", layout="wide")
st.title("AI Diagnostic Tool for Electrical Performance Monitoring")

tabs = st.tabs(["🔍 Analyze Telemetry", "📈 Generate Test Dataset"])

# ------------------------------------------------------------------
#  TAB 1  –  Upload & Analyze
# ------------------------------------------------------------------
with tabs[0]:
    st.header("Upload a CSV or Excel file")
    uploaded = st.file_uploader("Drag & drop or browse", type=["csv", "xlsx"])

    if uploaded:
        # Save to a temp file so run_model can read from disk
        suffix = Path(uploaded.name).suffix
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        tmp.write(uploaded.read()); tmp.close()

        # Run the model
        with st.spinner("Running anomaly detection …"):
            run_model(tmp.name)

        # Get the newest outputs folder
        newest = sorted(Path("outputs").glob("*_run*"), key=os.path.getmtime)[-1]
        st.success(f"Analysis complete!  Results in `{newest}`")

        # Show suggestions_only.csv directly in the app (if it exists)
        sug_file = newest / "suggestions_only.csv"
        if sug_file.exists():
            st.subheader("Flagged anomalies")
            df_sug = pd.read_csv(sug_file)
            st.dataframe(df_sug, use_container_width=True)
        else:
            st.info("No anomalies detected.")

        # Show plot image
        img_path = newest / "telemetry_with_anomalies.png"
        if img_path.exists():
            st.image(str(img_path), caption="Trend plot with anomalies", use_container_width=True)

# ------------------------------------------------------------------
# TAB 2 – Generate synthetic dataset
# ------------------------------------------------------------------
with tabs[1]:
    st.header("Create a synthetic test CSV")

    n_normal = st.slider("Normal points", 30, 300, 100)
    n_anom   = st.slider("Number of anomalies", 1, 20, 5)

    if st.button("Generate & Download"):
        # --------------- normal points ----------------------------
        start_ts = datetime.now().replace(microsecond=0, second=0)
        ts    = [start_ts + timedelta(seconds=i) for i in range(n_normal)]
        cur   = np.random.normal(1.6, 0.05, n_normal)
        volt  = np.random.normal(12.0, 0.08, n_normal)
        rpm   = np.random.normal(8000, 80,  n_normal)

        # --------------- INSERT anomalies at random positions ----
        for _ in range(n_anom):
            idx = np.random.randint(0, len(ts))      # random slot

            ts.insert(idx, ts[idx - 1] + timedelta(seconds=1))

            cur  = np.insert(cur,  idx, 3.5 + np.random.normal(0, 0.03))
            volt = np.insert(volt, idx, 11.7 + np.random.normal(0, 0.03))
            rpm  = np.insert(rpm,  idx, 2000 + np.random.normal(0, 50))

        # --------------- build DataFrame & download --------------
        df_gen = pd.DataFrame({
            "Date": ts,
            "Current": np.round(cur, 3),
            "Voltage": np.round(volt, 3),
            "speed_rpm": rpm.astype(int)
        })

        csv = df_gen.to_csv(index=False).encode()
        st.download_button(
            "Download CSV",
            data=csv,
            file_name="synthetic_telemetry.csv",
            mime="text/csv"
        )


        # Optional immediate analysis
        if st.checkbox("Run the model on this synthetic file now"):
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
            tmp.write(csv); tmp.close()
            run_model(tmp.name)
            newest = sorted(Path("outputs").glob("*_run*"), key=os.path.getmtime)[-1]
            st.success(f"Analysis complete! Results in `{newest}`")
            st.image(str(newest / "telemetry_with_anomalies.png"),
                     caption="Trend plot for synthetic data",
                     use_container_width=True)

st.markdown(
"> ⚠️ Suggestions are generated automatically for educational purposes only "
"and **do not** replace professional diagnostics."
)
