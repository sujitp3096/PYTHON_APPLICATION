import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "Pclass": [1, 3, 2, 1, 3, 2, 1, 3, 2, 1],
    "Age": [25, 30, 18, 40, 22, 35, 28, 19, 45, 50],
    "Fare": [80, 10, 30, 100, 15, 40, 90, 8, 35, 120],
    "FamilySize": [1, 4, 2, 1, 5, 3, 2, 6, 2, 1],
    "Survived": [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred) * 100, 2), "%")

print("\nEnter Passenger Details")

pclass = int(input("Passenger Class (1-3): "))
age = int(input("Age: "))
fare = float(input("Fare Paid: "))
family = int(input("Family Size: "))

result = model.predict([[pclass, age, fare, family]])

if result[0] == 1:
    print("\n✅ Passenger is likely to Survive")
else:
    print("\n❌ Passenger is unlikely to Survive")
