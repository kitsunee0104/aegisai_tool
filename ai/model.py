from sklearn.ensemble import IsolationForest
import numpy as np
import joblib
import os

MODEL_PATH = "ai/aegis_model.pkl"


def train_model(training_data):

    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    model.fit(training_data)

    joblib.dump(model, MODEL_PATH)


def load_model():

    if not os.path.exists(MODEL_PATH):
        raise Exception("Model not found. Run ai/train.py first.")

    return joblib.load(MODEL_PATH)


def predict(sample):

    model = load_model()

    sample = np.array(sample).reshape(1, -1)

    return model.predict(sample)[0]
