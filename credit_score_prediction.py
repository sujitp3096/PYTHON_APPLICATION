import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "Age": [22, 30, 40, 28, 35, 50, 45, 27, 38, 32],
    "Income": [25000, 50000, 80000, 30000, 60000, 100000, 90000, 35000, 70000, 55000],
    "LoanAmount": [5000, 10000, 20000, 7000, 15000, 25000, 18000, 6000, 17000, 12000],
    "MissedPayments": [5, 2, 0, 4, 1, 0, 1, 3, 0, 2],
    "CreditScore": [0, 1, 2, 0, 1, 2, 2, 0, 2, 1]
}

df = pd.DataFrame(data)

X = df.drop("CreditScore", axis=1)
y = df["CreditScore"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred) * 100, 2), "%")

print("\nCredit Score Categories")
print("0 = Poor")
print("1 = Average")
print("2 = Good")

age = int(input("\nEnter Age: "))
income = float(input("Enter Annual Income: "))
loan = float(input("Enter Loan Amount: "))
missed = int(input("Enter Missed Payments: "))

result = model.predict([[age, income, loan, missed]])

labels = ["Poor", "Average", "Good"]

print("\nPredicted Credit Score:", labels[result[0]])
