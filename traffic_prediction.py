import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample traffic dataset
data = {
    'Time': [8, 9, 10, 17, 18, 19, 12, 14],
    'DayType': [1, 1, 1, 1, 1, 1, 0, 0],   # 1 = Weekday, 0 = Weekend
    'Location': [1, 1, 2, 1, 2, 2, 0, 0], # 0=Residential,1=Office,2=Highway
    'Traffic': [2, 2, 1, 2, 2, 1, 0, 0]   # 0=Low,1=Medium,2=High
}

df = pd.DataFrame(data)

X = df[['Time', 'DayType', 'Location']]
y = df['Traffic']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# User input
print("Enter Traffic Details:")
time = int(input("Enter Time (0-23): "))
day = int(input("Enter Day Type (1=Weekday, 0=Weekend): "))
location = int(input("Location (0=Residential, 1=Office, 2=Highway): "))

# Prediction
prediction = model.predict([[time, day, location]])

# Output
if prediction[0] == 0:
    print("Predicted Traffic Level: LOW")
elif prediction[0] == 1:
    print("Predicted Traffic Level: MEDIUM")
else:
    print("Predicted Traffic Level: HIGH")
