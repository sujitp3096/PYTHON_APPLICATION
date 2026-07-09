import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Sample Dataset
data = {
    "Area": [600, 800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
    "Bedrooms": [1, 2, 2, 3, 3, 4, 4, 4, 5, 5],
    "Bathrooms": [1, 1, 2, 2, 2, 3, 3, 4, 4, 5],
    "Age": [10, 8, 6, 5, 4, 3, 2, 2, 1, 1],
    "Rent": [8000, 12000, 15000, 18000, 22000, 28000, 32000, 36000, 42000, 50000]
}

df = pd.DataFrame(data)

X = df[["Area", "Bedrooms", "Bathrooms", "Age"]]
y = df["Rent"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

prediction = model.predict(X_test)
print("R² Score:", round(r2_score(y_test, prediction), 2))

print("\nEnter House Details")

area = int(input("Area (sq ft): "))
bedrooms = int(input("Bedrooms: "))
bathrooms = int(input("Bathrooms: "))
age = int(input("House Age (years): "))

rent = model.predict([[area, bedrooms, bathrooms, age]])

print(f"\nEstimated Monthly Rent: ₹{rent[0]:,.0f}")
