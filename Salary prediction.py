
from sklearn.linear_model import LinearRegression
import numpy as np

experience = np.array([1,2,3,4,5]).reshape(-1,1)
salary = np.array([25000,30000,40000,50000,60000])

model = LinearRegression()
model.fit(experience, salary)

exp = float(input("Years of Experience: "))
print("Predicted Salary:", model.predict([[exp]])[0])
