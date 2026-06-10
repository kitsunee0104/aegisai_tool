import numpy as np

from ai.model import train_model
from utils.logger import log

def run_training():

    training_data = np.array([
        [4, 800, 20, 1, 5],
        [5, 900, 25, 0, 7],
        [3, 600, 18, 2, 4],
        [6, 1200, 30, 1, 9],
        [5, 1000, 24, 1, 6],
        [4, 850, 22, 0, 5],
        [5, 1100, 27, 1, 8]
    ])

    train_model(training_data)

    log("Model trained successfully")
    log("Model saved as ai/aegis_model.pkl")


if __name__ == "__main__":
    run_training()
