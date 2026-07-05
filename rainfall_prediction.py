import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "Temperature": [30, 35, 28, 25, 40, 32, 27, 31, 29, 38],
    "Humidity": [80, 45, 90, 95, 30, 60, 88, 55, 85, 35],
    "WindSpeed": [12, 8, 15, 10, 5, 7, 14, 9, 13, 6],
    "Rain": [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Temperature", "Humidity", "WindSpeed"]]
y = df["Rain"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred) * 100, 2), "%")

# User Input
temperature = float(input("\nEnter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))
wind = float(input("Enter Wind Speed (km/h): "))

result = model.predict([[temperature, humidity, wind]])

if result[0] == 1:
    print("\n🌧️ Rain is likely.")
else:
    print("\n☀️ No rain expected.")
