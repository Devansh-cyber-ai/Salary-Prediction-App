"""
Shared UI styles for the Salary Prediction App.
Import and call inject_css() at the top of every page.
"""

import streamlit as st

ACCENT_GRADIENT = "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
ACCENT_PRIMARY = "#667eea"
ACCENT_SECONDARY = "#764ba2"
SUCCESS_COLOR = "#00d4aa"
BG_PRIMARY = "#0a0a1a"
BG_CARD = "rgba(255, 255, 255, 0.03)"
BORDER_COLOR = "rgba(255, 255, 255, 0.08)"


def inject_css():
    """Inject the shared premium dark-theme CSS into the current page."""
    st.markdown(
        """
        <style>
        /* ─── Google Font ──────────────────────────────────────────── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        /* ─── Global ───────────────────────────────────────────────── */
        html, body, .stApp, [data-testid="stAppViewContainer"] {
            font-family: 'Inter', sans-serif !important;
        }
        .stApp {
            background: linear-gradient(160deg, #0a0a1a 0%, #0d0d24 40%, #111128 100%);
        }

        /* ─── Hide default Streamlit chrome ────────────────────────── */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stHeader"] {
            background: rgba(10, 10, 26, 0.8);
            backdrop-filter: blur(12px);
        }

        /* ─── Sidebar ──────────────────────────────────────────────── */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0d0d24 0%, #111128 100%) !important;
            border-right: 1px solid rgba(255,255,255,0.06);
        }
        [data-testid="stSidebar"] .stMarkdown p,
        [data-testid="stSidebar"] .stMarkdown li {
            color: #b0b0cc;
        }

        /* ─── Glassmorphism Card ───────────────────────────────────── */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 2rem;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .glass-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 40px rgba(102, 126, 234, 0.15);
        }

        /* ─── Gradient Heading ─────────────────────────────────────── */
        .gradient-heading {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
            font-size: 2.8rem;
            line-height: 1.2;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }
        .gradient-heading-sm {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 700;
            font-size: 1.6rem;
            line-height: 1.3;
            margin-bottom: 0.3rem;
        }

        /* ─── Subtitle ─────────────────────────────────────────────── */
        .subtitle {
            color: #8888aa;
            font-size: 1.15rem;
            font-weight: 400;
            margin-bottom: 2rem;
            line-height: 1.6;
        }

        /* ─── Buttons ──────────────────────────────────────────────── */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.7rem 2.5rem !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            font-family: 'Inter', sans-serif !important;
            letter-spacing: 0.02em;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.35) !important;
        }
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5) !important;
        }
        .stButton > button:active {
            transform: translateY(0px) !important;
        }

        /* ─── Select Boxes ─────────────────────────────────────────── */
        .stSelectbox > div > div {
            background: rgba(255, 255, 255, 0.04) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px !important;
            color: #e8e8f0 !important;
            font-family: 'Inter', sans-serif !important;
        }
        .stSelectbox label {
            color: #b0b0cc !important;
            font-weight: 500 !important;
            font-family: 'Inter', sans-serif !important;
        }

        /* ─── Expander ─────────────────────────────────────────────── */
        .streamlit-expanderHeader {
            background: rgba(255, 255, 255, 0.03) !important;
            border-radius: 10px !important;
            color: #b0b0cc !important;
            font-family: 'Inter', sans-serif !important;
        }

        /* ─── Result Card ──────────────────────────────────────────── */
        .result-card {
            background: linear-gradient(135deg, rgba(102,126,234,0.15) 0%, rgba(118,75,162,0.15) 100%);
            border: 1px solid rgba(102, 126, 234, 0.3);
            border-radius: 20px;
            padding: 2.5rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            animation: fadeInUp 0.6s ease-out;
        }
        .result-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -50%;
            width: 200%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.03), transparent);
            animation: shimmer 3s infinite;
        }
        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .result-label {
            color: #8888aa;
            font-size: 0.95rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 0.75rem;
        }
        .result-value {
            font-size: 3.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.2;
            margin-bottom: 0.5rem;
        }
        .result-subtitle {
            color: #6a6a88;
            font-size: 0.85rem;
            font-weight: 400;
        }

        /* ─── Metric Mini Cards ────────────────────────────────────── */
        .metric-row {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        }
        .metric-mini {
            flex: 1;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
            transition: border-color 0.3s ease;
        }
        .metric-mini:hover {
            border-color: rgba(102, 126, 234, 0.3);
        }
        .metric-mini .label {
            color: #6a6a88;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.4rem;
        }
        .metric-mini .value {
            color: #e8e8f0;
            font-size: 1.4rem;
            font-weight: 700;
        }
        .metric-mini .value.accent {
            color: #667eea;
        }
        .metric-mini .value.green {
            color: #00d4aa;
        }
        .metric-mini .value.purple {
            color: #a78bfa;
        }

        /* ─── Feature Importance Inline ────────────────────────────── */
        .feat-bar-container {
            margin: 0.4rem 0;
        }
        .feat-bar-label {
            color: #b0b0cc;
            font-size: 0.85rem;
            font-weight: 500;
            margin-bottom: 0.2rem;
        }
        .feat-bar-track {
            background: rgba(255,255,255,0.05);
            border-radius: 6px;
            height: 8px;
            overflow: hidden;
        }
        .feat-bar-fill {
            height: 100%;
            border-radius: 6px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transition: width 0.8s ease-out;
        }
        .feat-bar-pct {
            color: #6a6a88;
            font-size: 0.75rem;
            text-align: right;
            margin-top: 0.1rem;
        }

        /* ─── Badge / Tag ──────────────────────────────────────────── */
        .tag {
            display: inline-block;
            background: rgba(102, 126, 234, 0.15);
            color: #667eea;
            border: 1px solid rgba(102, 126, 234, 0.25);
            border-radius: 8px;
            padding: 0.3rem 0.8rem;
            font-size: 0.82rem;
            font-weight: 600;
            margin: 0.2rem 0.3rem 0.2rem 0;
        }
        .tag.green {
            background: rgba(0, 212, 170, 0.12);
            color: #00d4aa;
            border-color: rgba(0, 212, 170, 0.25);
        }
        .tag.purple {
            background: rgba(167, 139, 250, 0.12);
            color: #a78bfa;
            border-color: rgba(167, 139, 250, 0.25);
        }
        .tag.amber {
            background: rgba(251, 191, 36, 0.12);
            color: #fbbf24;
            border-color: rgba(251, 191, 36, 0.25);
        }

        /* ─── Divider ──────────────────────────────────────────────── */
        .styled-divider {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(102,126,234,0.3), transparent);
            margin: 2rem 0;
        }

        /* ─── Responsive ───────────────────────────────────────────── */
        @media (max-width: 768px) {
            .gradient-heading { font-size: 2rem; }
            .result-value { font-size: 2.4rem; }
            .metric-row { flex-direction: column; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = ""):
    """Render a gradient page header with optional subtitle."""
    st.markdown(f'<h1 class="gradient-heading">{title}</h1>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<p class="subtitle">{subtitle}</p>', unsafe_allow_html=True)


def glass_card_start():
    """Return opening HTML for a glassmorphism card."""
    return '<div class="glass-card">'


def glass_card_end():
    """Return closing HTML for a glassmorphism card."""
    return '</div>'


def styled_divider():
    """Render a gradient divider."""
    st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)


def render_result_card(salary: float):
    """Render the salary prediction result card with animation."""
    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-label">Estimated Annual Salary</div>
            <div class="result-value">₹{salary:,.2f} LPA</div>
            <div class="result-subtitle">Predicted by Random Forest model · 200 estimators · 5 features</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric_row(metrics: list[tuple[str, str, str]]):
    """Render a row of mini metric cards.
    
    Args:
        metrics: list of (label, value, css_class) tuples.
                 css_class is one of: '', 'accent', 'green', 'purple'.
    """
    cards = ""
    for label, value, css_cls in metrics:
        cards += (
            f'<div class="metric-mini">'
            f'<div class="label">{label}</div>'
            f'<div class="value {css_cls}">{value}</div>'
            f'</div>'
        )
    st.markdown(f'<div class="metric-row">{cards}</div>', unsafe_allow_html=True)


def render_feature_bars(importances: dict[str, float]):
    """Render horizontal feature-importance bars."""
    max_val = max(importances.values()) if importances else 1
    html = ""
    for name, val in sorted(importances.items(), key=lambda x: x[1], reverse=True):
        pct = (val / max_val) * 100
        html += f"""
        <div class="feat-bar-container">
            <div class="feat-bar-label">{name}</div>
            <div class="feat-bar-track">
                <div class="feat-bar-fill" style="width:{pct}%"></div>
            </div>
            <div class="feat-bar-pct">{val:.1%}</div>
        </div>
        """
    st.markdown(html, unsafe_allow_html=True)
