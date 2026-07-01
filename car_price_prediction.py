import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample Dataset
data = {
    "Year": [2018, 2019, 2020, 2021, 2022, 2017, 2016, 2023],
    "Kilometers": [50000, 40000, 30000, 20000, 10000, 70000, 80000, 5000],
    "Mileage": [18, 20, 22, 21, 23, 17, 16, 24],
    "Price": [500000, 600000, 700000, 800000, 900000, 450000, 400000, 1000000]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Year", "Kilometers", "Mileage"]]
y = df["Price"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("R² Score:", round(r2_score(y_test, pred), 2))

# User Input
year = int(input("Enter Car Year: "))
km = int(input("Enter Kilometers Driven: "))
mileage = float(input("Enter Mileage (km/l): "))

price = model.predict([[year, km, mileage]])

print(f"\nEstimated Car Price: ₹{price[0]:,.0f}")
