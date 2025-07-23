# AI as a Diagnostic Tool for Electrical Performance Monitoring

# WattWatcher-AI 🔌🤖

AI-based diagnostic tool for spotting electrical and motor faults from telemetry data.

WattWatcher-AI ingests *Voltage, Current,* and *RPM* telemetry, learns a “normal” pattern with an Isolation-Forest model, then:

## Features
- **Isolation-Forest anomaly detection** on Current, Voltage, RPM  
- **Plain-English suggestions** for each flagged issue (stall, voltage sag…)  (⚠️ **educational only**) 
- **Streamlit web interface** (upload files or generate synthetic test sets)  
- runs as a drag-and-drop **Streamlit** web app **or** a simple CLI
- **Timestamped output folders** with full CSV report, suggestions-only CSV, and trend plot  
- flags anomalies in real time  
- plots trends with red worry-spots  

## Dataset

When uploading your own dataset, it should be a .xlsx or a .csv file. 

The columns should be formatted as follows (case-sensitive):

| Date/Timestamp | Current | Voltage | speed_rpm |

If you are unsure of the formatting, run the web app and generate a sample dataset as a "testing" dataset

## Quick start
Run through Powershell/Terminal

```bash
git clone https://github.com/ACF808/wattwatcher-ai.git
cd wattwatcher-ai
python -m venv venv && .\venv\Scripts\activate        # Windows
# source venv/bin/activate                            # macOS / Linux
pip install -r requirements.txt
python -m streamlit run web_app.py
