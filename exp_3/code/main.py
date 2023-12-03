# features: sepalLength, sepalWidth, petalLength, petalWidth
# target: setosa (0), versicolor (1), virginica (2)
from knn import KNN
import util
import pandas as pd
from sklearn.model_selection import train_test_split


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
    print(f"Accuracy: {accuracy}")


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
    print(f"Accuracy: {accuracy}")


def irisDT():
    pass


def bankDT():
    pass


def main():
    # bankKNN(3)
    # irisKNN(3)
    irisDT()
    bankDT()


if __name__ == "__main__":
    main()
