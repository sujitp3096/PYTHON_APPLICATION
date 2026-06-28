import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "Age": [22, 35, 40, 28, 50, 32, 45, 27, 38, 30],
    "MonthlyBill": [300, 900, 1200, 450, 1500, 600, 1300, 500, 1000, 700],
    "Tenure": [2, 24, 36, 6, 48, 12, 40, 8, 30, 15],
    "SupportCalls": [5, 1, 0, 4, 0, 3, 1, 4, 2, 3],
    "Churn": [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Features and Target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# User Input
age = int(input("Enter Customer Age: "))
bill = float(input("Enter Monthly Bill: "))
tenure = int(input("Enter Months with Company: "))
calls = int(input("Enter Number of Support Calls: "))

result = model.predict([[age, bill, tenure, calls]])

if result[0] == 1:
    print("\n⚠️ Customer is likely to leave.")
else:
    print("\n✅ Customer is likely to stay.")
