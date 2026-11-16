from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from src.data.loaders import load_iris_dataset
from src.models.classical_svm import train_svm_rbf

# Load dataset
X, y, target_names = load_iris_dataset()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# Train model
model = train_svm_rbf(X_train, y_train)

# Evaluation
predictions = model.predict(X_test)

print("Best parameters:", model.best_params_)
print(classification_report(
    y_test,
    predictions,
    target_names=target_names
))