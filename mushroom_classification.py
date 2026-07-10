from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample dataset (using built-in dataset for demonstration)
data = load_breast_cancer()

X = data.data
y = data.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred) * 100, 2), "%")

print("\nEnter Sample Values")

values = []
for feature in data.feature_names:
    value = float(input(f"{feature}: "))
    values.append(value)

prediction = model.predict([values])

if prediction[0] == 1:
    print("\n🍄 Prediction: Edible Mushroom")
else:
    print("\n☠️ Prediction: Poisonous Mushroom")
