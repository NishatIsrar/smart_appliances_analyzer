# Smart Appliance Energy & Fault Analyzer

## Introduction

Smart Appliance Energy & Fault Analyzer is a Python-based project developed to analyze electrical parameters and identify abnormal operating conditions in a simulated household fan. It monitors voltage and current variations, calculates power and energy consumption, and detects potential faults using predefined thresholds.

The project also includes an interactive dashboard for visualizing measurements and summarizing detected faults.

## Key Features

* Voltage and current monitoring
* Power and energy consumption analysis
* Voltage drop and abnormal current detection
* Graphical representation of electrical parameters
* Data storage and analysis using CSV and SQLite
* Interactive dashboard for result visualization

## Technologies

Python · NumPy · Pandas · Matplotlib · SQLite · Streamlit

## Project Workflow

1. Generate simulated appliance readings.
2. Calculate power and energy consumption.
3. Identify abnormal voltage and current conditions.
4. Store readings in CSV and SQLite.
5. Visualize results through graphs and a dashboard.

## Execution

Install the required libraries:

```bash
py -m pip install numpy pandas matplotlib streamlit
```

Run the main program:

```bash
py main.py
```

Launch the dashboard:

```bash
py -m streamlit run app.py
```

Run `main.py` before launching the dashboard to generate the required data file.

## Fault Detection Thresholds

* **Voltage:** Below 210 V
* **Current:** Above 0.35 A

These thresholds are predefined for this project.

## Limitation

The project uses simulated data and is intended for educational and analytical purposes. It does not use real-time measurements from a physical appliance.

