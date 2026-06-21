"""
Salary Prediction Model — Training Pipeline
=============================================
Trains a Random Forest Regressor (200 estimators) on the India Job Market
2024-2026 dataset with 5 features: Job_Title, City, Experience_Level,
Education_Required, and Job_Type.

Usage:
    python train_model.py
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pickle

# ─── 1. Load Data ────────────────────────────────────────────────────────────
print("Loading dataset...")
df = pd.read_csv('india_job_market_2024_2026.csv')
print(f"  Loaded {len(df)} rows × {len(df.columns)} columns")

# ─── 2. Feature Selection ───────────────────────────────────────────────────
CATEGORICAL_FEATURES = ['Job_Title', 'City', 'Education_Required', 'Job_Type']
TARGET = 'Salary_LPA'

# Experience level → numeric midpoint mapping
EXPERIENCE_MAPPING = {
    'Fresher (0-1 yr)': 0.5,
    'Junior (1-3 yrs)': 2.0,
    'Mid (3-6 yrs)': 4.5,
    'Senior (6-10 yrs)': 8.0,
    'Lead (10+ yrs)': 12.0,
}

# ─── 3. Encode Features ─────────────────────────────────────────────────────
print("Encoding features...")

# OrdinalEncoder for each categorical feature
encoders = {}
for col in CATEGORICAL_FEATURES:
    enc = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
    df[f'{col}_enc'] = enc.fit_transform(df[[col]]).ravel()
    encoders[col] = enc
    print(f"  {col}: {len(enc.categories_[0])} categories")

# Experience: string → numeric
df['Experience_enc'] = df['Experience_Level'].map(EXPERIENCE_MAPPING)
print(f"  Experience_Level: {len(EXPERIENCE_MAPPING)} levels (numeric mapping)")

# ─── 4. Prepare Feature Matrix ──────────────────────────────────────────────
feature_columns = ['Job_Title_enc', 'City_enc', 'Experience_enc',
                   'Education_Required_enc', 'Job_Type_enc']
feature_names = ['Job_Title', 'City', 'Experience_Level',
                 'Education_Required', 'Job_Type']

X = df[feature_columns].values
y = df[TARGET].values

# ─── 5. Train/Test Split ────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
print(f"\nTrain set: {X_train.shape[0]} samples")
print(f"Test set:  {X_test.shape[0]} samples")

# ─── 6. Train Model ─────────────────────────────────────────────────────────
print("\nTraining Random Forest Regressor (n_estimators=200)...")
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1,
)
model.fit(X_train, y_train)

# ─── 7. Evaluate ────────────────────────────────────────────────────────────
y_pred = model.predict(X_test)
metrics = {
    'r2': float(r2_score(y_test, y_pred)),
    'mae': float(mean_absolute_error(y_test, y_pred)),
    'rmse': float(np.sqrt(mean_squared_error(y_test, y_pred))),
}

print("\n" + "=" * 50)
print("  MODEL EVALUATION RESULTS")
print("=" * 50)
print(f"  R2 Score : {metrics['r2']:.4f}")
print(f"  MAE      : INR {metrics['mae']:.2f} LPA")
print(f"  RMSE     : INR {metrics['rmse']:.2f} LPA")
print("=" * 50)

# Feature importances
print("\n  Feature Importances:")
for name, imp in sorted(zip(feature_names, model.feature_importances_),
                         key=lambda x: x[1], reverse=True):
    bar = "#" * int(imp * 40)
    print(f"    {name:<22s} {imp:.3f}  {bar}")

# ─── 8. Save Artifacts ──────────────────────────────────────────────────────
save_data = {
    'model': model,
    'encoders': encoders,           # dict of OrdinalEncoders
    'exp_mapping': EXPERIENCE_MAPPING,
    'metrics': metrics,
    'feature_names': feature_names,
}

with open('saved_steps.pkl', 'wb') as f:
    pickle.dump(save_data, f)

print(f"\n[OK] Model + encoders + metrics saved to saved_steps.pkl")
print(f"  File features: {feature_names}")
