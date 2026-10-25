import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# 1. Generate simulated fan data
time = np.arange(60)

voltage = 230 + np.random.normal(0, 1, 60)
voltage[30:40] = 200 + np.random.normal(0, 1, 10)

current = 0.26 + np.random.normal(0, 0.01, 60)
current[45:55] = 0.40 + np.random.normal(0, 0.01, 10)

# 2. Calculate power and energy
power = voltage * current
energy = power / 3600

# 3. Label conditions
condition = np.full(60, "Normal", dtype=object)
condition[30:40] = "Voltage Drop"
condition[45:55] = "Abnormal Current"

data = pd.DataFrame({
    "Time_s": time,
    "Voltage_V": voltage,
    "Current_A": current,
    "Power_W": power,
    "Energy_Wh": energy,
    "Condition": condition
})

# 4. Detect faults
voltage_drop = data["Voltage_V"] < 210
abnormal_current = data["Current_A"] > 0.35

print(data.head(10))
print(f"\nTotal Energy: {data['Energy_Wh'].sum():.3f} Wh")

print("\n--- Fault Summary ---")
print("Voltage Drop:", "Detected" if voltage_drop.any() else "Not Detected")
print("Abnormal Current:", "Detected" if abnormal_current.any() else "Not Detected")

overall_status = "FAULT DETECTED" if voltage_drop.any() or abnormal_current.any() else "NORMAL"
print("Overall Status:", overall_status)

# 5. Save data to CSV
data.to_csv("normal_fan_data.csv", index=False)

# 6. Store data in SQLite
connection = sqlite3.connect("appliance_data.db")
data.to_sql("fan_data", connection, if_exists="replace", index=False)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM fan_data")
print("Total readings in database:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM fan_data WHERE Condition = 'Voltage Drop'")
print("Voltage Drop readings:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM fan_data WHERE Condition = 'Abnormal Current'")
print("Abnormal Current readings:", cursor.fetchone()[0])

connection.close()
print("Fan data stored in SQLite database.")

# 7. Plot voltage
plt.figure()
plt.plot(time, voltage)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Fan Voltage During Normal and Fault Conditions")
plt.show()

# 8. Plot current
plt.figure()
plt.plot(time, current)
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("Fan Current During Normal and Fault Conditions")
plt.show()

# 9. Plot power with highlighted faults
plt.figure()
plt.plot(time, power, label="Power")
plt.axvspan(30, 40, color="orange", alpha=0.3, label="Voltage Drop")
plt.axvspan(45, 55, color="red", alpha=0.3, label="Abnormal Current")
plt.xlabel("Time (s)")
plt.ylabel("Power (W)")
plt.title("Fan Power with Fault Conditions")
plt.legend()
plt.show()
# Plot normal fan power consumption
plt.figure()
plt.plot(time, power)
plt.xlabel("Time (s)")
plt.ylabel("Power (W)")
plt.title("Normal Fan Power Consumption")
plt.show()