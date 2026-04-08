#!/usr/bin/env python3
"""
Complete ML Model Training Pipeline
Trains a Logistic Regression model on Bank Note Authentication data
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

print("=" * 70)
print("BANK NOTE AUTHENTICATION ML PIPELINE")
print("=" * 70)

# ============================================================================
# STEP 1: Load and Explore Data
# ============================================================================
print("\n📂 STEP 1: Loading Dataset...")
data = pd.read_csv('BankNote_Authentication.csv')
print(f"✅ Dataset loaded! Shape: {data.shape}")
print(f"\nFirst 5 rows:")
print(data.head())
print(f"\nDataset Info:")
print(data.info())
print(f"\nDescriptive Statistics:")
print(data.describe())
print(f"\nClass Distribution:")
print(data['class'].value_counts())

# ============================================================================
# STEP 2: Prepare Data - Train/Test Split
# ============================================================================
print("\n" + "=" * 70)
print("📊 STEP 2: Preparing Data - Train/Test Split...")
print("=" * 70)

X = data.drop('class', axis=1)
y = data['class']

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\n✅ Data split completed!")
print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")
print(f"\nTraining set class distribution:")
print(y_train.value_counts())
print(f"\nTesting set class distribution:")
print(y_test.value_counts())

# ============================================================================
# STEP 3: Train Logistic Regression Model
# ============================================================================
print("\n" + "=" * 70)
print("🤖 STEP 3: Training Logistic Regression Model...")
print("=" * 70)

model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

print(f"✅ Model training completed!")
print(f"Model coefficients shape: {model.coef_.shape}")
print(f"Model intercept: {model.intercept_[0]:.4f}")

# ============================================================================
# STEP 4: Evaluate Model Performance
# ============================================================================
print("\n" + "=" * 70)
print("📈 STEP 4: Evaluating Model Performance...")
print("=" * 70)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print(f"\nTraining Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy: {test_accuracy:.4f}")

print('\n' + '=' * 50)
print('CLASSIFICATION REPORT (Test Set)')
print('=' * 50)
print(classification_report(y_test, y_test_pred))

print('\n' + '=' * 50)
print('CONFUSION MATRIX (Test Set)')
print('=' * 50)
print(confusion_matrix(y_test, y_test_pred))

# ============================================================================
# STEP 5: Save the Trained Model
# ============================================================================
print("\n" + "=" * 70)
print("💾 STEP 5: Saving Trained Model...")
print("=" * 70)

joblib.dump(model, 'model.pkl')
print(f"✅ Model saved successfully as 'model.pkl'")

# Verify the file was saved
import os
if os.path.exists('model.pkl'):
    file_size = os.path.getsize('model.pkl')
    print(f"Model file size: {file_size:,} bytes")
    print(f"✅ File verification passed!")
else:
    print("❌ Error: model.pkl was not saved!")

# ============================================================================
# STEP 6: Model Summary
# ============================================================================
print("\n" + "=" * 70)
print("📋 MODEL SUMMARY")
print("=" * 70)
print(f"Model Type: Logistic Regression")
print(f"Features: 4 (variance, skewness, curtosis, entropy)")
print(f"Classes: 2 (0: Genuine, 1: Forged)")
print(f"Training Samples: {X_train.shape[0]}")
print(f"Testing Samples: {X_test.shape[0]}")
print(f"Train Accuracy: {train_accuracy:.4f} ({train_accuracy*100:.2f}%)")
print(f"Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")
print(f"Model File: model.pkl")

print("\n" + "=" * 70)
print("✅ PIPELINE COMPLETED SUCCESSFULLY!")
print("=" * 70)
print("\n📌 Next Steps:")
print("1. Start FastAPI server: uvicorn main:app --reload")
print("2. Visit API docs: http://127.0.0.1:8000/docs")
print("3. Test predictions using the Swagger UI")
print("\n" + "=" * 70)
