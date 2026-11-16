from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold

def train_svm_rbf(X_train, y_train):
    pipeline = make_pipeline(
        StandardScaler(),
        SVC(kernel="rbf")
    )

    params = {
        "svc__C": [0.1, 1, 10, 100],
        "svc__gamma": ["scale", 0.01, 0.1, 1]
    }

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    model = GridSearchCV(
        pipeline,
        params,
        cv=cv,
        scoring="accuracy"
    )

    model.fit(X_train, y_train)
    return model