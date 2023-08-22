# imports 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import time


# Sample dataset of questions and answers
questions = [
    "What is the capital of France?",
    "Who wrote Romeo and Juliet?",
    "What is the largest planet in our solar system?"
]

answers = [
    "The capital of France is Paris.",
    "Romeo and Juliet was written by William Shakespeare.",
    "Jupiter is the largest planet in our solar system."
]
start_time = time.time()
# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the questions into TF-IDF vectors
question_vectors = vectorizer.fit_transform(questions)

# User input
user_input = input("Ask:- ")

# Transform user input into a TF-IDF vector
user_input_vector = vectorizer.transform([user_input])

# Calculate cosine similarities between user input vector and question vectors
similarities = cosine_similarity(user_input_vector, question_vectors)

# Find the most similar question's index
most_similar_index = np.argmax(similarities)

# Retrieve the corresponding answer
response = answers[most_similar_index]

end_time = time.time()

elapsed_time = end_time - start_time
print("Elapsed Time:", elapsed_time, "seconds")
print("User Input:", user_input)
print("Answer:", response)
