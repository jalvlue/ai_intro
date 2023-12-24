# features: sepalLength, sepalWidth, petalLength, petalWidth
# target: setosa (0), versicolor (1), virginica (2)
from knn import KNN
from decisionTree import DecisionTreeClassifier
import util
import pandas as pd
from sklearn.model_selection import train_test_split

map = {
    "Iris-versicolor": 0,
    "Iris-setosa": 1,
    "Iris-virginica": 2,
}


def bankKNN(n=3):
    data = pd.read_csv("../data/bank+marketing/bank/bank.csv", delimiter=";")

    X = data.drop("y", axis=1)
    y = data["y"]

    X = pd.get_dummies(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    X_train = X_train.astype(int)
    X_test = X_test.astype(int)

    X_train_array = X_train.to_numpy()
    y_train_array = y_train.to_numpy()
    X_test_array = X_test.to_numpy()
    y_test_array = y_test.to_numpy()
    # print(X_test_array)
    # print(y_test_array)

    model = KNN(k=n)
    model.fit(X_train_array, y_train_array)

    y_pred = model.predict(X_test_array)

    accuracy = util.accuracy(y_test_array, y_pred)
    # print(f"Accuracy: {accuracy}")
    return accuracy


def irisKNN(n=3):
    headers = ["sepalLength", "sepalWidth", "petalLength", "petalWidth", "target"]
    data = pd.read_csv(
        "../data/iris/iris.data",
        delimiter=",",
        header=None,
        names=headers,
    )

    X = data.drop("target", axis=1)
    y = data["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    X_train = X_train.astype(float)
    X_test = X_test.astype(float)

    X_train = X_train.to_numpy()
    y_train = y_train.to_numpy()
    X_test = X_test.to_numpy()
    y_test = y_test.to_numpy()

    model = KNN(k=n)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = util.accuracy(y_test, y_pred)
    return accuracy
    # print(f"Accuracy: {accuracy}")


def irisDT(max_depth=3):
    headers = ["sepalLength", "sepalWidth", "petalLength", "petalWidth", "target"]
    data = pd.read_csv(
        "../data/iris/iris.data",
        delimiter=",",
        header=None,
        names=headers,
    )

    X = data.drop("target", axis=1)
    y = data["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    X_train = X_train.astype(float)
    X_test = X_test.astype(float)

    X_train = X_train.to_numpy()
    y_train = y_train.to_numpy()
    X_test = X_test.to_numpy()
    y_test = y_test.to_numpy()

    y_train = [map[i] for i in y_train]
    y_test = [map[i] for i in y_test]

    # print("DEBUG: ")
    # print(X_train)
    # print(y_train)

    model = DecisionTreeClassifier(max_depth)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = util.accuracy(y_test, y_pred)
    # print(f"Accuracy: {accuracy}")
    return accuracy


def bankDT(max_depth=3):
    data = pd.read_csv("../data/bank+marketing/bank/bank.csv", delimiter=";")

    X = data.drop("y", axis=1)
    y = data["y"]

    X = pd.get_dummies(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    X_train = X_train.astype(int)
    X_test = X_test.astype(int)

    X_train_array = X_train.to_numpy()
    y_train_array = y_train.to_numpy()
    X_test_array = X_test.to_numpy()
    y_test_array = y_test.to_numpy()

    model = DecisionTreeClassifier(max_depth)
    model.fit(X_train_array, y_train_array)

    y_pred = model.predict(X_test_array)

    accuracy = util.accuracy(y_test_array, y_pred)
    return accuracy
    # print(f"Accuracy: {accuracy}")


def main():
    # irisKNN(3)
    # bankKNN(3)
    # irisDT()
    # bankDT()

    accuracy_record = []
    for i in range(1, 100):
        accuracy_record.append(100 * irisKNN(i))
    util.accuracy_plot("knn", "iris", accuracy_record)

    accuracy_record = []
    for i in range(1, 100):
        accuracy_record.append(100 * bankKNN(i))
    util.accuracy_plot("knn", "bank", accuracy_record)

    accuracy_record = []
    for i in range(1, 30):
        accuracy_record.append(100 * irisDT(i))
    util.accuracy_plot("dt", "iris", accuracy_record)

    accuracy_record = []
    for i in range(1, 30):
        accuracy_record.append(100 * bankDT(i))
    util.accuracy_plot("dt", "bank", accuracy_record)


if __name__ == "__main__":
    main()
