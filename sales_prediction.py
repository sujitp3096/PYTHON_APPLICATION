import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample Dataset
data = {
    "TV": [230, 44, 17, 151, 180, 8, 57, 120, 200, 90],
    "Radio": [37, 39, 45, 41, 10, 48, 32, 25, 20, 35],
    "Newspaper": [69, 45, 70, 58, 20, 75, 23, 40, 30, 50],
    "Sales": [22.1, 10.4, 9.3, 18.5, 16.2, 7.2, 11.8, 15.5, 19.8, 13.2]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Model Performance
prediction = model.predict(X_test)
print("R² Score:", round(r2_score(y_test, prediction), 2))

# User Input
print("\nEnter Advertising Budget (in thousands)")

tv = float(input("TV Budget: "))
radio = float(input("Radio Budget: "))
newspaper = float(input("Newspaper Budget: "))

sales = model.predict([[tv, radio, newspaper]])

print(f"\n📈 Predicted Sales: {sales[0]:.2f} thousand units")
