import numpy as np


def euclidean_distance(point, data):
    distance = []
    for row in data:
        distance.append(np.sqrt(np.sum((point - row) ** 2)))

    return distance


def most_common(lst):
    return max(set(lst), key=lst.count)


def accuracy(y_test, y_pred):
    return sum([1 for y_t, y_p in zip(y_test, y_pred) if y_t == y_p]) / len(y_test)
