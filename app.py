import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Smart Appliance Energy & Fault Analyzer")

data = pd.read_csv("normal_fan_data.csv")

# Summary
total_energy = data["Energy_Wh"].sum()
voltage_fault = (data["Voltage_V"] < 210).any()
current_fault = (data["Current_A"] > 0.35).any()

col1, col2 = st.columns(2)

col1.metric("Total Energy", f"{total_energy:.3f} Wh")
col2.metric(
    "Appliance Status",
    "FAULT DETECTED" if voltage_fault or current_fault else "NORMAL"
)

# Voltage graph
st.subheader("Voltage Monitoring")
fig, ax = plt.subplots()
ax.plot(data["Time_s"], data["Voltage_V"])
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Voltage (V)")
st.pyplot(fig)
plt.close(fig)

# Current graph
st.subheader("Current Monitoring")
fig, ax = plt.subplots()
ax.plot(data["Time_s"], data["Current_A"])
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Current (A)")
st.pyplot(fig)
plt.close(fig)

# Fault summary
st.subheader("Fault Summary")
st.write("Voltage Drop:", "Detected" if voltage_fault else "Not Detected")
st.write("Abnormal Current:", "Detected" if current_fault else "Not Detected")