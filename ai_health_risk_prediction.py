def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def diabetes_risk(age, bmi, exercise):
    risk = 0

    if age > 45:
        risk += 2
    if bmi >= 25:
        risk += 2
    if exercise == "no":
        risk += 2

    if risk >= 5:
        return "High Risk"
    elif risk >= 3:
        return "Moderate Risk"
    else:
        return "Low Risk"


def obesity_risk(bmi, junk_food):
    risk = 0

    if bmi >= 30:
        risk += 3
    if junk_food == "yes":
        risk += 2

    if risk >= 4:
        return "High Risk"
    elif risk >= 2:
        return "Moderate Risk"
    else:
        return "Low Risk"


print("===== AI Health Risk Prediction System =====")

age = int(input("Enter Age: "))
bmi = float(input("Enter BMI: "))
exercise = input("Do you exercise regularly? (yes/no): ").lower()
junk_food = input("Do you eat junk food frequently? (yes/no): ").lower()

print("\n----- Health Analysis Report -----")
print("BMI Category       :", bmi_category(bmi))
print("Diabetes Risk      :", diabetes_risk(age, bmi, exercise))
print("Obesity Risk       :", obesity_risk(bmi, junk_food))

