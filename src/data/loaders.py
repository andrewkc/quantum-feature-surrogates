from sklearn.datasets import load_iris

def load_iris_dataset():
    iris = load_iris()
    return iris.data, iris.target, iris.target_names