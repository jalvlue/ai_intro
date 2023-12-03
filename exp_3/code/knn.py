from sklearn import neighbors
from util import accuracy, most_common, euclidean_distance
import numpy as np


class KNN:
    def __init__(self, k=5) -> None:
        self.k = k

    def fit(self, x, y):
        self.X_train = x
        self.y_train = y

    def predict(self, X_test):
        y_pred = []
        for row in X_test:
            neighbors_result = []
            distances = np.linalg.norm(self.X_train - row, axis=1)

            y_sorted = [
                y for _, y in sorted(zip(distances, self.y_train), key=lambda x: x[0])
            ]

            for i in range(self.k):
                neighbors_result.append(y_sorted[i])

            y_pred.append(most_common(neighbors_result))

        return y_pred
