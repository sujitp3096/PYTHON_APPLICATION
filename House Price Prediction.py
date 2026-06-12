from sklearn.linear_model import LinearRegression

area = [[500],[1000],[1500],[2000]]
price = [10,20,30,40]

model = LinearRegression()
model.fit(area, price)

new_area = int(input("Enter Area: "))
print("Price:", model.predict([[new_area]])[0])
