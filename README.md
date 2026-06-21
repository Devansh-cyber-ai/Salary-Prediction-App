<div align="center">

# 💰 Salary Prediction System

**Estimate your market value using Machine Learning — powered by 5,000+ real Indian job listings.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.58+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

*A machine-learning-powered salary estimation tool built for Indian developers and job seekers.*

</div>

## 🚀 Overview

The **Salary Prediction System** helps developers and job seekers estimate their annual salary (in ₹ LPA — Lakhs Per Annum) based on real-world hiring data from the Indian job market (2024–2026). It uses a **Random Forest Regressor** trained on 5,000+ job postings with a premium dark-themed UI built on Streamlit.

### ✨ Key Features

- **🎯 Salary Predictor** — Enter your job title, city, experience, education, and employment type to get an instant salary estimate
- **📊 Data Explorer** — 7 interactive Matplotlib charts with a custom dark theme for exploratory data analysis
- **📈 Model Insights** — View feature importances and performance metrics (R², MAE, RMSE) in real time
- **ℹ️ About Page** — Dataset details, model architecture, and tech stack overview
- **🌙 Premium Dark UI** — Glassmorphism cards, gradient headings, and smooth animations

## 📸 Pages

| Page | Description |
|------|-------------|
| **Salary Predictor** | Main prediction page — select your profile and get an estimated salary |
| **Data Explorer** | EDA dashboard with salary distributions, city comparisons, experience breakdowns, top-paying roles, and more |
| **About** | Project overview, dataset stats, model architecture, and tech stack |

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.10+ |
| **Web Framework** | Streamlit |
| **ML Model** | Random Forest Regressor (scikit-learn) |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib |
| **Encoding** | OrdinalEncoder (scikit-learn) |

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Devansh-cyber-ai/Salary-Prediction-App.git
   cd Salary-Prediction-App
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model** (generates `saved_steps.pkl`)
   ```bash
   python train_model.py
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

   The app will open at `http://localhost:8501`.

## 📂 Project Structure

```
Salary-Prediction-App/
├── app.py                        # Main prediction page
├── train_model.py                # Model training pipeline
├── styles.py                     # Custom CSS & UI components
├── india_job_market_2024_2026.csv  # Training dataset
├── saved_steps.pkl               # Trained model + encoders (generated)
├── explore.ipynb                 # Jupyter notebook for EDA
├── requirements.txt              # Python dependencies
├── .streamlit/
│   └── config.toml               # Streamlit theme configuration
└── pages/
    ├── 1_Data_Explorer.py        # EDA dashboard with 7 charts
    └── 2_About.py                # Project info & tech stack
```

## 🧠 Model Details

| Parameter | Value |
|-----------|-------|
| **Algorithm** | Random Forest Regressor |
| **Estimators** | 200 decision trees |
| **Test Split** | 80/20 train/test |
| **Random State** | 42 |

### Input Features

| Feature | Description | Categories |
|---------|-------------|------------|
| **Job Title** | Role/designation | 30 unique roles (AI Engineer, Backend Developer, DevOps, etc.) |
| **City** | Job location | 17 Indian cities + Remote |
| **Experience Level** | Seniority band | Fresher · Junior · Mid · Senior · Lead |
| **Education** | Required qualification | 8 levels (BCA to PhD) |
| **Employment Type** | Work arrangement | Full-Time · Contract · Part-Time · Internship |

### Target Variable

- **Salary_LPA** — Annual salary in Lakhs Per Annum (₹)

## 📊 Dataset

The model is trained on the **India Job Market 2024–2026** dataset containing real-world job listings scraped from major Indian hiring platforms.

- **5,000+** job listings
- **30** unique job titles
- **17** cities + Remote
- **5** experience levels
- **8** education levels
- **4** employment types

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

**Built with ❤️ by [Devansh](https://github.com/Devansh-cyber-ai)**

</div>
