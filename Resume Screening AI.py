skills = ["python", "machine learning", "sql"]

resume = input("Paste Resume Text: ").lower()

score = sum(1 for skill in skills if skill in resume)

print("Match Score:", score, "/", len(skills))
