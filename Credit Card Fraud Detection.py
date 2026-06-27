import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "Amount": [100, 5000, 250, 10000, 150, 8000, 400, 12000, 350, 9000],
    "TransactionTime": [10, 22, 14, 2, 9, 1, 16, 3, 12, 5],
    "LocationRisk": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    "International": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    "Fraud": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Features and Target
X = df.drop("Fraud", axis=1)
y = df["Fraud"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test Accuracy
predictions = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, predictions))

# User Input
amount = float(input("Enter Transaction Amount: "))
time = int(input("Enter Transaction Hour (0-23): "))
location = int(input("Location Risk (0=Safe, 1=Risky): "))
international = int(input("International Transaction? (0=No, 1=Yes): "))

result = model.predict([[amount, time, location, international]])

if result[0] == 1:
    print("\n⚠️ Fraudulent Transaction Detected!")
else:
    print("\n✅ Genuine Transaction")
