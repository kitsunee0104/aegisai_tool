import os
import joblib
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), "aegis_model.pkl")

def train_default_model():
    from sklearn.ensemble import IsolationForest

    model = IsolationForest()

    data = np.array([
        [4, 800, 20, 1, 5],
        [5, 900, 25, 0, 7],
        [3, 600, 18, 2, 4],
        [6, 1200, 30, 1, 9],
        [5, 1000, 24, 1, 6],
        [4, 850, 22, 0, 5],
        [5, 1100, 27, 1, 8]
    ])

    model.fit(data)
    joblib.dump(model, MODEL_PATH)

    print("[+] Initial model trained and saved")

def load_model():
    if not os.path.exists(MODEL_PATH):
        print("[+] No model found. Initializing AegisAI engine...")
        train_default_model()

    return joblib.load(MODEL_PATH)


def predict(sample):
    model = load_model()
    return model.predict([sample])[0]
