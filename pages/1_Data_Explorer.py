"""
Data Explorer — Matplotlib-powered EDA page
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pickle
from styles import inject_css, page_header, render_metric_row, styled_divider

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Data Explorer · Salary Prediction",
    page_icon="📊",
    layout="wide",
)
inject_css()

# ─── Chart theme ─────────────────────────────────────────────────────────────
CHART_COLORS = {
    "gradient_start": "#667eea",
    "gradient_end": "#764ba2",
    "accent": "#667eea",
    "success": "#00d4aa",
    "purple": "#a78bfa",
    "pink": "#f093fb",
    "amber": "#fbbf24",
    "bg": "#0a0a1a",
    "card": "#111128",
    "text": "#b0b0cc",
    "text_bright": "#e8e8f0",
    "grid": (1.0, 1.0, 1.0, 0.06),
}

# Build a gradient palette for bar charts
_cmap = plt.cm.colors.LinearSegmentedColormap.from_list(
    "accent", [CHART_COLORS["gradient_start"], CHART_COLORS["gradient_end"]]
)


def _apply_dark_style(ax, fig):
    """Apply the app's dark theme to a matplotlib axes & figure."""
    fig.patch.set_facecolor(CHART_COLORS["bg"])
    ax.set_facecolor(CHART_COLORS["card"])
    ax.tick_params(colors=CHART_COLORS["text"], labelsize=9)
    ax.xaxis.label.set_color(CHART_COLORS["text"])
    ax.yaxis.label.set_color(CHART_COLORS["text"])
    ax.title.set_color(CHART_COLORS["text_bright"])
    for spine in ax.spines.values():
        spine.set_color(CHART_COLORS["grid"])
    ax.grid(axis="y", color=CHART_COLORS["grid"], linewidth=0.5)


# ─── Load Data ───────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    return pd.read_csv("india_job_market_2024_2026.csv")


@st.cache_resource
def load_model_data():
    with open("saved_steps.pkl", "rb") as f:
        return pickle.load(f)


df = load_data()
model_data = load_model_data()

# ─── Hero ────────────────────────────────────────────────────────────────────
page_header(
    "Data Explorer",
    "Dive into the India Job Market 2024-2026 dataset. "
    "Every chart uses Matplotlib with a custom dark theme."
)

# ─── Quick Stats ─────────────────────────────────────────────────────────────
render_metric_row([
    ("Total Listings", f"{len(df):,}", "accent"),
    ("Job Titles", f"{df['Job_Title'].nunique()}", "green"),
    ("Cities", f"{df['City'].nunique()}", "purple"),
    ("Avg Salary", f"₹{df['Salary_LPA'].mean():.1f} LPA", "accent"),
])

st.markdown("<br>", unsafe_allow_html=True)

# ─── 1. Salary Distribution ─────────────────────────────────────────────────
styled_divider()
st.markdown('<p class="gradient-heading-sm">1 · Salary Distribution</p>', unsafe_allow_html=True)

fig1, ax1 = plt.subplots(figsize=(10, 4.5))
_apply_dark_style(ax1, fig1)

n, bins, patches = ax1.hist(
    df["Salary_LPA"], bins=40, edgecolor="none", alpha=0.9
)
# Color each bar with gradient
for i, p in enumerate(patches):
    p.set_facecolor(_cmap(i / len(patches)))

ax1.axvline(df["Salary_LPA"].mean(), color=CHART_COLORS["success"],
            linestyle="--", linewidth=1.5, label=f'Mean: ₹{df["Salary_LPA"].mean():.1f} LPA')
ax1.axvline(df["Salary_LPA"].median(), color=CHART_COLORS["amber"],
            linestyle="--", linewidth=1.5, label=f'Median: ₹{df["Salary_LPA"].median():.1f} LPA')
ax1.set_xlabel("Salary (LPA)", fontsize=11, fontweight=500)
ax1.set_ylabel("Count", fontsize=11, fontweight=500)
ax1.set_title("Distribution of Salaries Across All Listings", fontsize=13, fontweight=600, pad=12)
ax1.legend(facecolor=CHART_COLORS["card"], edgecolor=CHART_COLORS["grid"],
           labelcolor=CHART_COLORS["text"], fontsize=9)
fig1.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

# ─── 2. Salary by Experience ────────────────────────────────────────────────
styled_divider()
st.markdown('<p class="gradient-heading-sm">2 · Salary by Experience Level</p>', unsafe_allow_html=True)

exp_order = ["Fresher (0-1 yr)", "Junior (1-3 yrs)", "Mid (3-6 yrs)",
             "Senior (6-10 yrs)", "Lead (10+ yrs)"]
exp_data = [df[df["Experience_Level"] == e]["Salary_LPA"].values for e in exp_order]

fig2, ax2 = plt.subplots(figsize=(10, 4.5))
_apply_dark_style(ax2, fig2)

bp = ax2.boxplot(
    exp_data,
    tick_labels=[e.split(" (")[0] for e in exp_order],
    patch_artist=True,
    widths=0.5,
    showfliers=False,
    medianprops=dict(color=CHART_COLORS["amber"], linewidth=2),
    whiskerprops=dict(color=CHART_COLORS["text"]),
    capprops=dict(color=CHART_COLORS["text"]),
)
for i, box in enumerate(bp["boxes"]):
    box.set_facecolor(_cmap(i / (len(exp_order) - 1)))
    box.set_edgecolor(CHART_COLORS["text"])
    box.set_alpha(0.85)

ax2.set_ylabel("Salary (LPA)", fontsize=11, fontweight=500)
ax2.set_title("Salary Range by Experience Level", fontsize=13, fontweight=600, pad=12)
fig2.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

# ─── 3. Top 10 Highest Paying Job Titles ────────────────────────────────────
styled_divider()
st.markdown('<p class="gradient-heading-sm">3 · Top 10 Highest Paying Roles</p>', unsafe_allow_html=True)

top_titles = (
    df.groupby("Job_Title")["Salary_LPA"]
    .median()
    .sort_values(ascending=True)
    .tail(10)
)

fig3, ax3 = plt.subplots(figsize=(10, 5))
_apply_dark_style(ax3, fig3)

colors3 = [_cmap(i / (len(top_titles) - 1)) for i in range(len(top_titles))]
bars = ax3.barh(top_titles.index, top_titles.values, color=colors3, height=0.6, edgecolor="none")
for bar, val in zip(bars, top_titles.values):
    ax3.text(val + 0.3, bar.get_y() + bar.get_height() / 2,
             f"₹{val:.1f}", va="center", color=CHART_COLORS["text_bright"],
             fontsize=9, fontweight=600)
ax3.set_xlabel("Median Salary (LPA)", fontsize=11, fontweight=500)
ax3.set_title("Top 10 Highest Paying Job Titles (by Median)", fontsize=13, fontweight=600, pad=12)
fig3.tight_layout()
st.pyplot(fig3)
plt.close(fig3)

# ─── 4. Salary by City ──────────────────────────────────────────────────────
styled_divider()
st.markdown('<p class="gradient-heading-sm">4 · Salary by City</p>', unsafe_allow_html=True)

city_median = df.groupby("City")["Salary_LPA"].median().sort_values(ascending=True)

fig4, ax4 = plt.subplots(figsize=(10, 5.5))
_apply_dark_style(ax4, fig4)

colors4 = [_cmap(i / (len(city_median) - 1)) for i in range(len(city_median))]
bars4 = ax4.barh(city_median.index, city_median.values, color=colors4, height=0.6)
for bar, val in zip(bars4, city_median.values):
    ax4.text(val + 0.2, bar.get_y() + bar.get_height() / 2,
             f"₹{val:.1f}", va="center", color=CHART_COLORS["text_bright"],
             fontsize=9, fontweight=600)
ax4.set_xlabel("Median Salary (LPA)", fontsize=11, fontweight=500)
ax4.set_title("Median Salary by City", fontsize=13, fontweight=600, pad=12)
fig4.tight_layout()
st.pyplot(fig4)
plt.close(fig4)

# ─── 5. Salary by Education ─────────────────────────────────────────────────
styled_divider()
st.markdown('<p class="gradient-heading-sm">5 · Salary by Education Level</p>', unsafe_allow_html=True)

edu_order = df.groupby("Education_Required")["Salary_LPA"].median().sort_values().index.tolist()
edu_data = [df[df["Education_Required"] == e]["Salary_LPA"].values for e in edu_order]

fig5, ax5 = plt.subplots(figsize=(10, 4.5))
_apply_dark_style(ax5, fig5)

bp5 = ax5.boxplot(
    edu_data,
    tick_labels=edu_order,
    patch_artist=True,
    widths=0.5,
    showfliers=False,
    medianprops=dict(color=CHART_COLORS["amber"], linewidth=2),
    whiskerprops=dict(color=CHART_COLORS["text"]),
    capprops=dict(color=CHART_COLORS["text"]),
)
for i, box in enumerate(bp5["boxes"]):
    box.set_facecolor(_cmap(i / max(len(edu_order) - 1, 1)))
    box.set_edgecolor(CHART_COLORS["text"])
    box.set_alpha(0.85)

ax5.set_ylabel("Salary (LPA)", fontsize=11, fontweight=500)
ax5.set_title("Salary Range by Education Level", fontsize=13, fontweight=600, pad=12)
plt.xticks(rotation=30, ha="right")
fig5.tight_layout()
st.pyplot(fig5)
plt.close(fig5)

# ─── 6. Feature Importance ──────────────────────────────────────────────────
styled_divider()
st.markdown('<p class="gradient-heading-sm">6 · Model Feature Importance</p>', unsafe_allow_html=True)

model = model_data["model"]
feat_names = model_data["feature_names"]
importances = model.feature_importances_
sorted_idx = np.argsort(importances)

fig6, ax6 = plt.subplots(figsize=(10, 4))
_apply_dark_style(ax6, fig6)

colors6 = [_cmap(i / (len(feat_names) - 1)) for i in range(len(sorted_idx))]
ax6.barh(
    [feat_names[i] for i in sorted_idx],
    importances[sorted_idx],
    color=colors6,
    height=0.5,
)
for i, idx in enumerate(sorted_idx):
    ax6.text(importances[idx] + 0.005, i,
             f"{importances[idx]:.1%}", va="center",
             color=CHART_COLORS["text_bright"], fontsize=10, fontweight=600)

ax6.set_xlabel("Importance", fontsize=11, fontweight=500)
ax6.set_title("Random Forest Feature Importance", fontsize=13, fontweight=600, pad=12)
ax6.xaxis.set_major_formatter(mticker.PercentFormatter(1.0))
fig6.tight_layout()
st.pyplot(fig6)
plt.close(fig6)

# ─── 7. Salary by Employment Type ───────────────────────────────────────────
styled_divider()
st.markdown('<p class="gradient-heading-sm">7 · Salary by Employment Type</p>', unsafe_allow_html=True)

jt_order = ["Full-Time", "Contract", "Part-Time", "Internship"]
jt_data = [df[df["Job_Type"] == jt]["Salary_LPA"].values for jt in jt_order]

fig7, ax7 = plt.subplots(figsize=(8, 4.5))
_apply_dark_style(ax7, fig7)

bp7 = ax7.boxplot(
    jt_data,
    tick_labels=jt_order,
    patch_artist=True,
    widths=0.45,
    showfliers=False,
    medianprops=dict(color=CHART_COLORS["amber"], linewidth=2),
    whiskerprops=dict(color=CHART_COLORS["text"]),
    capprops=dict(color=CHART_COLORS["text"]),
)
jt_colors = [CHART_COLORS["accent"], CHART_COLORS["purple"],
             CHART_COLORS["pink"], CHART_COLORS["success"]]
for box, c in zip(bp7["boxes"], jt_colors):
    box.set_facecolor(c)
    box.set_alpha(0.7)
    box.set_edgecolor(CHART_COLORS["text"])

ax7.set_ylabel("Salary (LPA)", fontsize=11, fontweight=500)
ax7.set_title("Salary Range by Employment Type", fontsize=13, fontweight=600, pad=12)
fig7.tight_layout()
st.pyplot(fig7)
plt.close(fig7)

st.markdown("<br><br>", unsafe_allow_html=True)
