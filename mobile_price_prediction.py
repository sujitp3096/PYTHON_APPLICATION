import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Sample Datase
data = {
    "RAM": [4, 6, 8, 12, 4, 8, 6, 12, 16, 8],
    "Storage": [64, 128, 128, 256, 32, 256, 64, 512, 512, 256],
    "Camera": [48, 64, 108, 200, 13, 50, 48, 108, 200, 64],
    "Battery": [5000, 5000, 6000, 5000, 4000, 6000, 4500, 5000, 6000, 5000],
    "Price": [15000, 22000, 30000, 60000, 10000, 35000, 18000, 70000, 85000, 40000]
}

df = pd.DataFrame(data)

X = df[["RAM", "Storage", "Camera", "Battery"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

prediction = model.predict(X_test)
print("R² Score:", round(r2_score(y_test, prediction), 2))

print("\nEnter Mobile Specifications")

ram = int(input("RAM (GB): "))
storage = int(input("Storage (GB): "))
camera = int(input("Camera (MP): "))
battery = int(input("Battery (mAh): "))

price = model.predict([[ram, storage, camera, battery]])

print(f"\nEstimated Mobile Price: ₹{price[0]:,.0f}")
