import pickle
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a decision tree classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the trained model to a file
model_filename = "decision_tree_model.pkl"
with open(model_filename, "wb") as file:
    pickle.dump(model, file)

print(f"Model saved as {model}")
