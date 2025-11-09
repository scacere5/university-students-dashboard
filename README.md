
# University Students Dashboard

An interactive Streamlit dashboard that summarizes university admissions, enrollment, retention, and satisfaction over time.

## Files
- `app.py`: Streamlit app source code.
- `university_student_data.csv`: Dataset used in the dashboard.
- `requirements.txt`: Python dependencies for deployment (Streamlit Cloud reads this).
- `colab_notebook.ipynb`: Google Colab starter notebook for EDA and plots.
- `report_template.md`: 1-page report template for your findings + links.

## Local run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## How to deploy on Streamlit Cloud
1. Push these files to a **public GitHub repository** (top level of the repo).
2. Go to https://streamlit.io/cloud and log in.
3. Click **Deploy an app** → **From existing repo**.
4. Select your repo and set **Main file path** to `app.py`.
5. Click **Deploy**. Streamlit Cloud auto-installs `requirements.txt` and launches the app.
6. Verify the app loads and filters/graphs work.

## Data
The app reads `university_student_data.csv` in the repo root. If you rename or move it, update the path inside `app.py`.

## Team
Samuel Caceres 
