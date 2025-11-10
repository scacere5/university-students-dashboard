
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="University Students Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("university_student_data.csv")
    if "Year" in df.columns:
        df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    return df

df = load_data()

st.title("🎓 University Admissions, Enrollment, Retention & Satisfaction")

with st.expander("About this dashboard"):
    st.write(
        """
        This dashboard summarizes student applications, admissions, enrollment, retention and satisfaction across years and terms.
        Use the filters in the sidebar to explore specific years, terms, and departments. By Samuel Caceres.
        """
    )

years = sorted(df["Year"].dropna().unique())
terms = sorted(df["Term"].dropna().unique())

st.sidebar.header("Filters")
year_sel = st.sidebar.multiselect("Year", years, default=years)
term_sel = st.sidebar.multiselect("Term", terms, default=terms)

dept_options = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
dept_sel = st.sidebar.multiselect("Department(s)", dept_options, default=dept_options)

f = df[df["Year"].isin(year_sel) & df["Term"].isin(term_sel)].copy()

col1, col2, col3, col4 = st.columns(4)
total_apps = int(f["Applications"].sum())
admit_rate = (f["Admitted"].sum() / f["Applications"].sum()) * 100 if f["Applications"].sum() else 0
avg_retention = f["Retention Rate (%)"].mean() if "Retention Rate (%)" in f.columns else None
avg_satisfaction = f["Student Satisfaction (%)"].mean() if "Student Satisfaction (%)" in f.columns else None

col1.metric("Total Applications", f"{total_apps:,}")
col2.metric("Admission Rate", f"{admit_rate:.1f}%")
col3.metric("Avg. Retention", f"{avg_retention:.1f}%" if avg_retention is not None else "N/A")
col4.metric("Avg. Satisfaction", f"{avg_satisfaction:.1f}%" if avg_satisfaction is not None else "N/A")

st.divider()

st.subheader("Retention Rate Trends Over Time")
if "Retention Rate (%)" in f.columns:
    retention = f.groupby(["Year"], as_index=False)["Retention Rate (%)"].mean().sort_values("Year")
    fig1, ax1 = plt.subplots()
    sns.lineplot(data=retention, x="Year", y="Retention Rate (%)", marker="o", ax=ax1)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Retention Rate (%)")
    ax1.set_title("Average Retention Rate by Year")
    ax1.grid(True, linestyle="--", alpha=0.4)
    st.pyplot(fig1)
else:
    st.info("Column 'Retention Rate (%)' not found.")

st.subheader("Student Satisfaction Scores by Year")
if "Student Satisfaction (%)" in f.columns:
    sat = f.groupby(["Year"], as_index=False)["Student Satisfaction (%)"].mean().sort_values("Year")
    fig2, ax2 = plt.subplots()
    sns.barplot(data=sat, x="Year", y="Student Satisfaction (%)", ax=ax2)
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Satisfaction (%)")
    ax2.set_title("Average Satisfaction by Year")
    for container in ax2.containers:
        ax2.bar_label(container, fmt="%.1f")
    st.pyplot(fig2)
else:
    st.info("Column 'Student Satisfaction (%)' not found.")

st.subheader("Spring vs Fall Comparison (Enrolled)")
if "Enrolled" in f.columns:
    term_comp = f.groupby(["Year", "Term"], as_index=False)["Enrolled"].sum()
    fig3, ax3 = plt.subplots()
    sns.lineplot(data=term_comp, x="Year", y="Enrolled", hue="Term", marker="o", ax=ax3)
    ax3.set_xlabel("Year")
    ax3.set_ylabel("Enrolled Students")
    ax3.set_title("Enrolled: Spring vs Fall")
    ax3.grid(True, linestyle="--", alpha=0.4)
    st.pyplot(fig3)
else:
    st.info("Column 'Enrolled' not found.")

st.divider()

st.subheader("Department Enrollment Distribution")
dept_data = f[dept_sel].sum().sort_values(ascending=False) if dept_sel else pd.Series(dtype=float)
if not dept_data.empty:
    fig4, ax4 = plt.subplots()
    wedges, texts, autotexts = ax4.pie(
        dept_data.values,
        labels=dept_data.index,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops={"width": 0.5}
    )
    ax4.set_title("Share of Enrolled Students by Department")
    ax4.axis("equal")
    st.pyplot(fig4)
else:
    st.info("Select at least one department in the sidebar to see the distribution.")

st.caption("Data source: university_student_data.csv")
