from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Test Accuracy
predictions = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")

print("\nFlower Types:")
for i, flower in enumerate(iris.target_names):
    print(f"{i} - {flower}")

# User Input
sepal_length = float(input("\nSepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

print("\nPredicted Flower:", iris.target_names[prediction[0]])
