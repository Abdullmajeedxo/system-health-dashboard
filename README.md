System Health Dashboard

A simple dashboard I built to monitor CPU, RAM, and disk usage in real time. The idea came from wanting to practice the kind of proactive monitoring that helps catch issues (like a disk filling up) before they actually cause problems.

🔗  Try it [https://system-health-dashboard-ghhnlz9vappye4zndv56f9h.streamlit.app/]

What it does
- Shows live CPU, RAM, and disk usage with color-coded gauges (green/orange/red depending on how close you are to trouble)
- Pops up an alert if anything crosses 85% usage
- Has a manual refresh button to pull fresh numbers

 Built with
Python, Streamlit, psutil, and Plotly for the gauges.

Running it yourself
```
pip install -r requirements.txt
streamlit run app.py
