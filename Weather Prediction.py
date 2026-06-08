from sklearn.tree import DecisionTreeRegressor

temp = [[25],[30],[35],[40]]
humidity = [60,50,40,30]

model = DecisionTreeRegressor()
model.fit(temp, humidity)

t = int(input("Temperature: "))
print("Predicted Humidity:", model.predict([[t]])[0])
