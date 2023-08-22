from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Sample data
documents = ["This is a positive document.", "This document is negative."]
labels = [1, 0]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(documents, labels, test_size=0.2, random_state=42, shuffle=True)

# Create and fit the TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)

# Create and fit the LogisticRegression model
logreg_model = LogisticRegression()
logreg_model.fit(X_train_tfidf, y_train)

# Transform test data using the same vectorizer
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Predict using the trained LogisticRegression model
predictions = logreg_model.predict(X_test_tfidf)
