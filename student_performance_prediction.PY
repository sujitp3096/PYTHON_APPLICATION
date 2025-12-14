def predict_performance(marks, attendance):
    score = (marks * 0.7) + (attendance * 0.3)

    if score >= 85:
        return "PASS", "Grade A"
    elif score >= 70:
        return "PASS", "Grade B"
    elif score >= 50:
        return "PASS", "Grade C"
    else:
        return "FAIL", "Grade D"


print("===== Student Performance Prediction System =====")

marks = float(input("Enter previous exam marks (0-100): "))
attendance = float(input("Enter attendance percentage (0-100): "))

status, grade = predict_performance(marks, attendance)

print("\n----- Prediction Result -----")
print("Result :", status)
print("Grade  :", grade)
