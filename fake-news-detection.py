import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "News": [
        "Government launches new education policy",
        "Scientists discover water on Mars",
        "Aliens landed in New York yesterday",
        "Free iPhone for everyone click here",
        "India wins cricket world cup",
        "Earth will end tomorrow",
        "New metro line opens in city",
        "Earn one lakh per day without work"
    ],
    "Label": [
        "Real",
        "Real",
        "Fake",
        "Fake",
        "Real",
        "Fake",
        "Real",
        "Fake"
    ]
}

df = pd.DataFrame(data)

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["News"])
y = df["Label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# User input
news = input("\nEnter a news headline: ")

news_vector = vectorizer.transform([news])
result = model.predict(news_vector)

print("\nPrediction:", result[0])
