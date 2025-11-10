
# University Students Dashboard

An interactive Streamlit dashboard that visualizes key university performance metrics — applications, admissions, enrollment, retention, and student satisfaction — over time.
This project is part of Activity 1 – Data Visualization and Dashboard Deployment.

## Files
- `app.py`: Streamlit app source code.
- `university_student_data.csv`: Dataset used in the dashboard.
- `requirements.txt`: Python dependencies for deployment (Streamlit Cloud reads this).
- `colab_notebook.ipynb`: Google Colab starter notebook for EDA and plots.
- `report_template.md`: 1-page report template for your findings + links.

## Overview

This dashboard enables users to explore institutional data using interactive filters for Year, Term (Spring/Fall), and Department.
It provides both summary indicators (KPIs) and visual insights to better understand trends and performance across semesters.

Key visualizations include:

📈 Retention Rate Trends over the years
📊 Student Satisfaction Scores by academic year
🔄 Spring vs Fall Enrollment Comparison
🥧 Department Enrollment Distribution (Engineering, Business, Arts, Science)

## How to deploy on Streamlit Cloud
1. Push these files to a **public GitHub repository** (top level of the repo).
2. Go to https://streamlit.io/cloud and log in.
3. Click **Deploy an app** → **From existing repo**.
4. Select your repo and set **Main file path** to `app.py`.
5. Click **Deploy**. Streamlit Cloud auto-installs `requirements.txt` and launches the app.
6. Verify the app loads and filters/graphs work.

## Data
The app reads `university_student_data.csv` in the repo root. If you rename or move it, update the path inside `app.py`.

## Only member
Samuel Caceres 
