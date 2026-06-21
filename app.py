"""
Salary Prediction System — Main Prediction Page
"""

import streamlit as st
import pickle
import numpy as np
from styles import inject_css, page_header, render_result_card, render_metric_row, render_feature_bars, styled_divider

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Salary Prediction System",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

# ─── Sidebar Branding ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding: 1rem 0 0.5rem 0;">
            <div style="font-size:2.5rem; margin-bottom:0.3rem;">💰</div>
            <div style="font-size:1.1rem; font-weight:700; color:#e8e8f0;
                        letter-spacing:-0.01em;">Salary Predictor</div>
            <div style="font-size:0.78rem; color:#6a6a88; margin-top:0.2rem;">
                Powered by Machine Learning
            </div>
        </div>
        <hr style="border:none; height:1px;
                   background:linear-gradient(90deg, transparent,
                   rgba(102,126,234,0.3), transparent); margin:1rem 0;">
        """,
        unsafe_allow_html=True,
    )

# ─── Load Model ─────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    with open("saved_steps.pkl", "rb") as f:
        return pickle.load(f)

data = load_model()
model = data["model"]
encoders = data["encoders"]
exp_mapping = data["exp_mapping"]
metrics = data["metrics"]
feature_names = data["feature_names"]

# ─── Hero Section ────────────────────────────────────────────────────────────
page_header(
    "Salary Prediction System",
    "Estimate your market value based on real-world Indian job market data. "
    "Powered by a Random Forest model trained on 5,000+ job postings."
)

# ─── Input Form ──────────────────────────────────────────────────────────────
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown(
    '<p class="gradient-heading-sm">🎯 Enter Your Details</p>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2, gap="large")

with col1:
    title_options = list(encoders["Job_Title"].categories_[0])
    title = st.selectbox("Job Title", title_options, index=0)

    education_options = list(encoders["Education_Required"].categories_[0])
    education = st.selectbox("Education Level", education_options, index=2)

    exp_labels = list(exp_mapping.keys())
    experience_choice = st.selectbox("Experience Level", exp_labels, index=2)

with col2:
    city_options = list(encoders["City"].categories_[0])
    city = st.selectbox("City", city_options, index=1)

    job_type_options = list(encoders["Job_Type"].categories_[0])
    job_type = st.selectbox("Employment Type", job_type_options, index=0)

st.markdown("</div>", unsafe_allow_html=True)

# ─── Predict ─────────────────────────────────────────────────────────────────
col_btn, _ = st.columns([1, 3])
with col_btn:
    predict_clicked = st.button("🚀  Calculate Salary", use_container_width=True)

if predict_clicked:
    # Encode inputs
    title_enc = encoders["Job_Title"].transform([[title]])[0][0]
    city_enc = encoders["City"].transform([[city]])[0][0]
    education_enc = encoders["Education_Required"].transform([[education]])[0][0]
    job_type_enc = encoders["Job_Type"].transform([[job_type]])[0][0]
    experience_enc = exp_mapping[experience_choice]

    X_new = np.array([[title_enc, city_enc, experience_enc, education_enc, job_type_enc]])
    predicted_salary = model.predict(X_new)[0]

    st.markdown("<br>", unsafe_allow_html=True)
    render_result_card(predicted_salary)

    # ─── Feature Importance Breakdown ────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)

    styled_divider()

    st.markdown(
        '<p class="gradient-heading-sm">📊 What Drives This Prediction?</p>',
        unsafe_allow_html=True,
    )

    importances = dict(zip(feature_names, model.feature_importances_))
    render_feature_bars(importances)

    # ─── Model Performance ───────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📈 Model Performance Metrics"):
        render_metric_row([
            ("R² Score", f"{metrics['r2']:.4f}", "green"),
            ("MAE", f"₹{metrics['mae']:.2f} LPA", "accent"),
            ("RMSE", f"₹{metrics['rmse']:.2f} LPA", "purple"),
        ])
        st.markdown(
            """
            <div style="color:#6a6a88; font-size:0.8rem; margin-top:1rem; line-height:1.6;">
                <strong>R²</strong> — proportion of variance explained (closer to 1 is better)<br>
                <strong>MAE</strong> — average absolute error in LPA<br>
                <strong>RMSE</strong> — root mean squared error, penalizes large errors
            </div>
            """,
            unsafe_allow_html=True,
        )