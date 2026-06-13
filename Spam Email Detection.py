from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = ["Win money now", "Hello friend", "Claim prize", "Meeting tomorrow"]
labels = [1,0,1,0]

cv = CountVectorizer()
X = cv.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

msg = input("Enter message: ")
result = model.predict(cv.transform([msg]))

print("Spam" if result[0] else "Not Spam")
