import os
import joblib
import numpy as np
from sklearn.ensemble import IsolationForest

# =========================
# MODEL PATH (inside package)
# =========================
MODEL_PATH = os.path.join(os.path.dirname(__file__), "aegis_model.pkl")


# =========================
# TRAIN DEFAULT MODEL
# =========================
def train_default_model():
    """
    Creates a baseline anomaly detection model
    (used on first run if no model exists)
    """

    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )

    training_data = np.array([
        [4, 800, 20, 1, 5],
        [5, 900, 25, 0, 7],
        [3, 600, 18, 2, 4],
        [6, 1200, 30, 1, 9],
        [5, 1000, 24, 1, 6],
        [4, 850, 22, 0, 5],
        [5, 1100, 27, 1, 8]
    ])

    model.fit(training_data)

    # Save model INSIDE package directory
    joblib.dump(model, MODEL_PATH)

    print("[+] AegisAI: Initial model trained and saved")


# =========================
# LOAD MODEL (FIXED)
# =========================
def load_model():
    """
    Loads trained model.
    If missing → auto initializes model (NO MANUAL TRAINING REQUIRED)
    """

    if not os.path.exists(MODEL_PATH):
        print("[+] Model not found. Initializing AegisAI engine...")
        train_default_model()

    return joblib.load(MODEL_PATH)


# =========================
# PREDICTION
# =========================
def predict(sample):
    """
    Returns:
    1  → Normal
   -1  → Anomaly
    """

    model = load_model()
    sample = np.array(sample).reshape(1, -1)

    return model.predict(sample)[0]
