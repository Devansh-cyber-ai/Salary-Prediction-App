"""
About — Project overview, dataset info, and tech stack
"""

import streamlit as st
import pandas as pd
import pickle
from styles import inject_css, page_header, render_metric_row, styled_divider

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="About · Salary Prediction",
    page_icon="ℹ️",
    layout="wide",
)
inject_css()

# ─── Load data for stats ────────────────────────────────────────────────────
@st.cache_resource
def load_model_data():
    with open("saved_steps.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_data
def load_data():
    return pd.read_csv("india_job_market_2024_2026.csv")

model_data = load_model_data()
df = load_data()
metrics = model_data["metrics"]

# ─── Hero ────────────────────────────────────────────────────────────────────
page_header(
    "About This Project",
    "A machine-learning-powered salary estimation tool built for Indian developers and job seekers."
)

# ─── Project Overview ────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="glass-card">
        <p class="gradient-heading-sm">🎯 Project Overview</p>
        <p style="color:#b0b0cc; line-height:1.8; font-size:0.95rem;">
            The <strong style="color:#e8e8f0;">Salary Prediction System</strong>
            helps developers and job seekers estimate their market value based on
            real-world hiring data from the Indian job market (2024–2026). It uses a
            <strong style="color:#667eea;">Random Forest Regressor</strong> trained
            on 5,000+ job postings to predict annual salaries in
            <strong style="color:#00d4aa;">₹ LPA</strong> (Lakhs Per Annum) based on
            five key factors: job title, city, experience level, education, and
            employment type.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─── Dataset ─────────────────────────────────────────────────────────────────
styled_divider()

st.markdown(
    """
    <div class="glass-card">
        <p class="gradient-heading-sm">📦 Dataset</p>
        <p style="color:#b0b0cc; line-height:1.8; font-size:0.95rem;">
            The model is trained on the
            <strong style="color:#e8e8f0;">India Job Market 2024–2026</strong>
            dataset, which contains real-world job listings scraped from major
            Indian hiring platforms.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

render_metric_row([
    ("Total Listings", f"{len(df):,}", "accent"),
    ("Features Used", "5", "green"),
    ("Total Columns", f"{len(df.columns)}", "purple"),
    ("Salary Range", f"₹{df['Salary_LPA'].min():.1f} – {df['Salary_LPA'].max():.1f} LPA", "accent"),
])

st.markdown("<br>", unsafe_allow_html=True)

# Feature details
st.markdown(
    """
    <div class="glass-card">
        <p class="gradient-heading-sm">🔑 Input Features</p>
        <table style="width:100%; color:#b0b0cc; border-collapse:collapse; font-size:0.9rem;">
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                <td style="padding:0.7rem 0; font-weight:600; color:#e8e8f0; width:30%;">Job Title</td>
                <td style="padding:0.7rem 0;">30 unique roles — AI Engineer, Backend Developer, DevOps, etc.</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                <td style="padding:0.7rem 0; font-weight:600; color:#e8e8f0;">City</td>
                <td style="padding:0.7rem 0;">17 Indian cities + Remote</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                <td style="padding:0.7rem 0; font-weight:600; color:#e8e8f0;">Experience Level</td>
                <td style="padding:0.7rem 0;">Fresher · Junior · Mid · Senior · Lead</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                <td style="padding:0.7rem 0; font-weight:600; color:#e8e8f0;">Education</td>
                <td style="padding:0.7rem 0;">8 levels from BCA to PhD</td>
            </tr>
            <tr>
                <td style="padding:0.7rem 0; font-weight:600; color:#e8e8f0;">Employment Type</td>
                <td style="padding:0.7rem 0;">Full-Time · Contract · Part-Time · Internship</td>
            </tr>
        </table>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─── Model Architecture ─────────────────────────────────────────────────────
styled_divider()

st.markdown(
    """
    <div class="glass-card">
        <p class="gradient-heading-sm">🧠 Model Architecture</p>
        <p style="color:#b0b0cc; line-height:1.8; font-size:0.95rem; margin-bottom:1rem;">
            The model is a <strong style="color:#667eea;">Random Forest Regressor</strong>
            from scikit-learn — an ensemble of 200 decision trees that independently
            vote on the predicted salary, reducing overfitting and improving
            generalisation.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

render_metric_row([
    ("Algorithm", "Random Forest", "accent"),
    ("Estimators", "200 trees", "green"),
    ("R² Score", f"{metrics['r2']:.4f}", "green"),
    ("MAE", f"₹{metrics['mae']:.2f} LPA", "purple"),
])

# ─── Tech Stack ──────────────────────────────────────────────────────────────
styled_divider()

st.markdown(
    """
    <div class="glass-card">
        <p class="gradient-heading-sm">🛠️ Tech Stack</p>
        <div style="margin-top:0.8rem;">
            <span class="tag">Python</span>
            <span class="tag green">Streamlit</span>
            <span class="tag purple">Scikit-learn</span>
            <span class="tag">Pandas</span>
            <span class="tag amber">NumPy</span>
            <span class="tag green">Matplotlib</span>
        </div>
        <table style="width:100%; color:#b0b0cc; border-collapse:collapse;
                       font-size:0.9rem; margin-top:1.2rem;">
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                <td style="padding:0.6rem 0; font-weight:600; color:#e8e8f0; width:30%;">Language</td>
                <td style="padding:0.6rem 0;">Python 3.14</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                <td style="padding:0.6rem 0; font-weight:600; color:#e8e8f0;">Web Framework</td>
                <td style="padding:0.6rem 0;">Streamlit (interactive data apps)</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                <td style="padding:0.6rem 0; font-weight:600; color:#e8e8f0;">ML Model</td>
                <td style="padding:0.6rem 0;">Random Forest Regressor (scikit-learn)</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                <td style="padding:0.6rem 0; font-weight:600; color:#e8e8f0;">Data Processing</td>
                <td style="padding:0.6rem 0;">Pandas, NumPy</td>
            </tr>
            <tr>
                <td style="padding:0.6rem 0; font-weight:600; color:#e8e8f0;">Visualization</td>
                <td style="padding:0.6rem 0;">Matplotlib (7 charts in Data Explorer)</td>
            </tr>
        </table>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br><br>", unsafe_allow_html=True)
