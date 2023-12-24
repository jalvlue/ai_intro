import numpy as np


class DecisionNode:
    def __init__(
        self,
        feature=None,
        threshold=None,
        value=None,
        true_branch=None,
        false_branch=None,
    ):
        self.feature = feature
        self.threshold = threshold
        self.value = value
        self.true_branch = true_branch
        self.false_branch = false_branch


class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def gini_index(self, groups, classes):
        n_instances = float(sum(len(group) for group in groups))
        gini = 0.0
        for group in groups:
            size = float(len(group))
            if size == 0:
                continue
            score = 0.0
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            gini += (1.0 - score) * (size / n_instances)
        return gini

    def split_data(self, dataset, feature, threshold):
        left, right = [], []
        if isinstance(threshold, int) or isinstance(threshold, float):
            for row in dataset:
                if row[feature] < threshold:
                    left.append(row)
                else:
                    right.append(row)
        else:
            for row in dataset:
                if row[feature] == threshold:
                    left.append(row)
                else:
                    right.append(row)
        return left, right

    def get_best_split(self, dataset):
        class_values = list(set(row[-1] for row in dataset))
        best_index, best_value, best_score, best_groups = 999, 999, 999, None
        for index in range(len(dataset[0]) - 1):
            unique_values = set(row[index] for row in dataset)
            for value in unique_values:
                groups = self.split_data(dataset, index, value)
                gini = self.gini_index(groups, class_values)
                if gini < best_score:
                    best_index = index
                    best_value = value
                    best_score = gini
                    best_groups = groups
        return {"index": best_index, "value": best_value, "groups": best_groups}

    def to_terminal(self, group):
        outcomes = [row[-1] for row in group]
        return max(set(outcomes), key=outcomes.count)

    def split(self, node, depth):
        left, right = node["groups"]
        del node["groups"]
        if not left or not right:
            node["true_branch"] = node["false_branch"] = self.to_terminal(left + right)
            return
        if self.max_depth is not None and depth >= self.max_depth:
            node["true_branch"] = self.to_terminal(left)
            node["false_branch"] = self.to_terminal(right)
            return
        if len(left) <= 1:
            node["true_branch"] = self.to_terminal(left)
        else:
            node["true_branch"] = self.get_best_split(left)
            self.split(node["true_branch"], depth + 1)
        if len(right) <= 1:
            node["false_branch"] = self.to_terminal(right)
        else:
            node["false_branch"] = self.get_best_split(right)
            self.split(node["false_branch"], depth + 1)

    def build_tree(self, train_data):
        root = self.get_best_split(train_data)
        self.split(root, 1)
        return root

    def fit(self, X, y):
        train_data = np.column_stack((X, y))
        self.tree = self.build_tree(train_data)

    def predict_node(self, node, row):
        if isinstance(row[node["index"]], int) or isinstance(row[node["index"]], float):
            if row[node["index"]] < node["value"]:
                if isinstance(node["true_branch"], dict):
                    return self.predict_node(node["true_branch"], row)
                else:
                    return node["true_branch"]
            else:
                if isinstance(node["false_branch"], dict):
                    return self.predict_node(node["false_branch"], row)
                else:
                    return node["false_branch"]
        else:
            if row[node["index"]] == node["value"]:
                if isinstance(node["true_branch"], dict):
                    return self.predict_node(node["true_branch"], row)
                else:
                    return node["true_branch"]
            else:
                if isinstance(node["false_branch"], dict):
                    return self.predict_node(node["false_branch"], row)
                else:
                    return node["false_branch"]

    def predict(self, X):
        predictions = []
        for row in X:
            prediction = self.predict_node(self.tree, row)
            predictions.append(prediction)
        return predictions
