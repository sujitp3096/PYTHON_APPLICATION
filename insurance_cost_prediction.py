import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample Dataset
data = {
    "Age": [18, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "BMI": [22, 24, 28, 30, 26, 31, 29, 33, 27, 35],
    "Children": [0, 1, 2, 1, 3, 2, 2, 4, 3, 5],
    "Smoker": [0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    "InsuranceCost": [3000, 5000, 12000, 15000, 8000, 18000, 10000, 22000, 12000, 25000]
}

df = pd.DataFrame(data)

# Features & Target
X = df[["Age", "BMI", "Children", "Smoker"]]
y = df["InsuranceCost"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y
