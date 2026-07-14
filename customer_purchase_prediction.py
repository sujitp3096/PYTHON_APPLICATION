import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "Age": [20, 25, 30, 35, 40, 45, 50, 28, 32, 38],
    "Salary": [25000, 35000, 50000, 65000, 80000, 95000, 110000, 45000, 60000, 75000],
    "Visits": [2, 3, 5, 7, 8, 10, 12, 4, 6, 9],
    "Purchased": [0, 0, 1, 1, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Age", "Salary", "Visits"]]
y = df["Purchased"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred) * 100, 2), "%")

# User Input
print("\nEnter Customer Details")

age = int(input("Age: "))
salary = float(input("Salary: "))
visits = int(input("Website Visits: "))

result = model.predict([[age, salary, visits]])

if result[0] == 1:
    print("\n🛒 Customer is likely to Purchase.")
else:
    print("\n❌ Customer is unlikely to Purchase.")
