import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(point, data):
    distance = []
    for row in data:
        distance.append(np.sqrt(np.sum((point - row) ** 2)))

    return distance


def most_common(lst):
    return max(set(lst), key=lst.count)


def accuracy(y_test, y_pred):
    return sum([1 for y_t, y_p in zip(y_test, y_pred) if y_t == y_p]) / len(y_test)


def accuracy_plot(algo, dataset, accuracy_records):
    plt.figure(figsize=(10, 6))

    nums = range(1, len(accuracy_records) + 1)
    plt.plot(nums, accuracy_records)

    if algo == "knn":
        plt.xlabel("Number of Neighbors (k)")
    if algo == "dt":
        plt.xlabel("Maximum Depth")

    plt.ylabel("Accuracy")
    plt.title(dataset + " on " + algo)
    plt.show()
