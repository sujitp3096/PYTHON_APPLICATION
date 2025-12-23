import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    'DayType': [1, 1, 0, 0, 1, 0, 1],        # 1 = Weekday, 0 = Weekend
    'Weather': [1, 0, 1, 2, 2, 0, 1],       # 0 = Rainy, 1 = Normal, 2 = Sunny
    'PastSales': [120, 100, 180, 200, 150, 90, 160],
    'Demand': [130, 110, 190, 210, 160, 100, 170]
}

df = pd.DataFrame(data)

X = df[['DayType', 'Weather', 'PastSales']]
y = df['Demand']

# Train model
model = LinearRegression()
model.fit(X, y)

# User input
print("Enter Food Demand Details:")
day = int(input("Day Type (1=Weekday, 0=Weekend): "))
weather = int(input("Weather (0=Rainy, 1=Normal, 2=Sunny): "))
past_sales = int(input("Past Sales Count: "))

# Prediction
prediction = model.predict([[day, weather, past_sales]])

print("Predicted Food Demand:", int(prediction[0]))
