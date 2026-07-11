from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = load_breast_cancer()   # Built-in dataset

X = data.data
y = data.target

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy
prediction = model.predict(X_test)
print("Model Accuracy:", round(accuracy_score(y_test, prediction) * 100, 2), "%")

print("\nEnter Patient Details")

values = []

for feature in data.feature_names:
    value = float(input(f"{feature}: "))
    values.append(value)

result = model.predict([values])

if result[0] == 1:
    print("\n❤️ Low Risk")
else:
    print("\n⚠️ High Risk")
