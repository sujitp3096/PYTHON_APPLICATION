from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
wine = load_wine()

X = wine.data
y = wine.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Test Accuracy
predictions = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")

# Feature Names
print("\nEnter the following values:")
values = []

for feature in wine.feature_names:
    value = float(input(f"{feature}: "))
    values.append(value)

# Predict
result = model.predict([values])

print("\nPredicted Wine Class:", result[0])
