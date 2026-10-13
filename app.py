import psutil
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="System Health Dashboard", layout="wide")

st.title("🖥️ System Health Dashboard")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def get_cpu_usage():

    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent, mem.used, mem.total

def get_disk_usage(path="C:\\"):
    disk = psutil.disk_usage(path)
    return disk.percent, disk.used, disk.total

def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)

def make_gauge(value, title):
    
    if value < 60:
        color = "green"
    elif value < 85:
        color = "orange"
    else:
        color = "red"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={"text": title},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": color},
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    return fig

col1, col2, col3 = st.columns(3)

with col1:
    cpu = get_cpu_usage()
    st.plotly_chart(make_gauge(cpu, "CPU Usage (%)"), use_container_width=True)

with col2:
    ram_percent, ram_used, ram_total = get_memory_usage()
    st.plotly_chart(make_gauge(ram_percent, "RAM Usage (%)"), use_container_width=True)
    st.caption(f"{bytes_to_gb(ram_used)} GB used / {bytes_to_gb(ram_total)} GB total")

with col3:
    disk_percent, disk_used, disk_total = get_disk_usage()
    st.plotly_chart(make_gauge(disk_percent, "Disk Usage (%)"), use_container_width=True)
    st.caption(f"{bytes_to_gb(disk_used)} GB used / {bytes_to_gb(disk_total)} GB total")

st.divider()
st.subheader("⚠️ Alerts")

alerts = []
if cpu > 85:
    alerts.append(f"High CPU usage: {cpu}%")
if ram_percent > 85:
    alerts.append(f"High RAM usage: {ram_percent}%")
if disk_percent > 85:
    alerts.append(f"Low disk space: {disk_percent}% used")

if alerts:
    for a in alerts:
        st.error(a)
else:
    st.success("All systems normal.")

if st.button("🔄 Refresh now"):
    st.rerun()
