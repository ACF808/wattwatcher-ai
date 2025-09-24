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

### Windows
#### Run through Powershell/Terminal

Prior to installing the model, ensure you have git installed on your computer by running this command in powershell
'''bash
git --version
'''

If you get an error, install the latest version of git at the website linked below, if not, skip to the installation
https://git-scm.com/downloads/win

Once it is installed, proceed with the installation of the model.

In order to install the model, paste this into powershell (first time only)
```bash
git clone https://github.com/ACF808/wattwatcher-ai.git
```

Once that's done installing, paste the following script into Powershell and hit enter. The requirements will take a few minutes to fully install the first time so be patient.
```bash
cd wattwatcher-ai
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m streamlit run web_app.py
```

### macOS
#### Run through Terminal

Paste this script and click return

**idk how to do mac, still figuring it out, work-in-progress :(

