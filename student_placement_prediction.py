import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "CGPA": [6.5, 7.2, 8.5, 9.1, 5.8, 7.8, 8.9, 6.9, 9.4, 7.0],
    "Aptitude": [60, 70, 85, 95, 50, 75, 90, 65, 98, 72],
    "Communication": [55, 68, 80, 92, 48, 74, 88, 60, 95, 70],
    "Placed": [0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["CGPA", "Aptitude", "Communication"]]
y = df["Placed"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Model Accuracy:", round(accuracy_score(y_test, pred) * 100, 2), "%")

# User Input
cgpa = float(input("\nEnter CGPA: "))
aptitude = int(input("Enter Aptitude Score: "))
communication = int(input("Enter Communication Score: "))

result = model.predict([[cgpa, aptitude, communication]])

if result[0] == 1:
    print("\n🎉 Student is Likely to be Placed.")
else:
    print("\n❌ Student is Not Likely to be Placed.")
