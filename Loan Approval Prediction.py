import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "Income": [25000, 50000, 70000, 45000, 80000, 35000, 90000, 60000],
    "LoanAmount": [100000, 200000, 250000, 150000, 300000, 120000, 350000, 180000],
    "CreditScore": [650, 750, 800, 700, 850, 680, 900, 720],
    "Employment": ["No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes"],
    "Approved": ["No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

# Encode Categorical Columns
encoder = LabelEncoder()
df["Employment"] = encoder.fit_transform(df["Employment"])
df["Approved"] = encoder.fit_transform(df["Approved"])

# Features and Target
X = df.drop("Approved", axis=1)
y = df["Approved"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

# User Input
income = float(input("Enter Income: "))
loan = float(input("Enter Loan Amount: "))
credit = int(input("Enter Credit Score: "))
employment = input("Employment (Yes/No): ")

employment = 1 if employment.lower() == "yes" else 0

result = model.predict([[income, loan, credit, employment]])

if result[0] == 1:
    print("✅ Loan Approved")
else:
    print("❌ Loan Rejected")
