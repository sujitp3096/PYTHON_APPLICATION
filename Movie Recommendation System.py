from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

movies = pd.DataFrame({
    'title': ['Avatar', 'Titanic', 'Avengers', 'Iron Man'],
    'genre': ['Sci-Fi', 'Romance', 'Action', 'Action']
})

cv = CountVectorizer()
matrix = cv.fit_transform(movies['genre'])
similarity = cosine_similarity(matrix)

movie = "Avengers"
index = movies[movies['title'] == movie].index[0]

scores = list(enumerate(similarity[index]))
scores = sorted(scores, key=lambda x: x[1], reverse=True)

for i in scores[1:]:
    print(movies.iloc[i[0]]['title'])
