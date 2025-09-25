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

# Quick start

## Windows (Run through Powershell/Terminal)

### Prerequisites

Before installing and running the project, make sure the following tools are installed. Run each command below in PowerShell. If you see an error for any step, follow the installation link provided.

```bash
# Check if Git is installed
git --version
```
If you get an error, install Git from: https://git-scm.com/downloads

After installation, restart PowerShell and run the command again.

```bash
# Check if Python is installed
python --version
```
If you get an error, install Python from: https://www.python.org/downloads/windows/

Make sure to check the box that says "Add Python to PATH" during installation.
After installation, restart PowerShell and try again.

```bash
# Check if pip (Python’s package manager) is installed
pip --version
```
If pip is not recognized, it likely means Python wasn't added to PATH correctly.
Reinstall Python and make sure the "Add to PATH" option is selected.

Once you’ve confirmed all of the above are working, you can proceed to install and run the project below.

### Installation

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




