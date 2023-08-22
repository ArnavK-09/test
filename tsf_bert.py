import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the Universal Sentence Encoder model
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Pre-fit answers
answers = [
    "Discord is a communication platform that allows users to create servers and communicate through text, voice, and video.",
    "To create a server, click on the '+' icon in the server column, choose 'Create a Server,' and follow the prompts.",
    "You can generate an invite link for your server and share it with your friends. Right-click the server name, choose 'Invite People,' and send the link.",
    "Yes, users must be at least 13 years old to use Discord. This is in compliance with COPPA regulations.",
    "Yes, you can download the Discord app on your mobile device from the app store.",
    "To create channels, right-click the server name, choose 'Create Channel,' and configure the settings.",
    "Roles are used to assign permissions to users within a server. You can create roles with different privileges.",
    "Click on your profile picture, then click 'Change Avatar' to upload a new picture.",
    "Yes, the limit for a group direct voice call is 25 participants, while for a server voice channel, it depends on the server's boost level.",
    "Yes, you can video chat with others using Discord's video call feature."
]

# User question
user_question = input("Ask -> ")

# Encode the user question and pre-fit answers
encoded_user_question = embed([user_question])[0]
encoded_answers = embed(answers)

# Calculate cosine similarity
similarity_scores = cosine_similarity(
    [encoded_user_question], encoded_answers)[0]

# Find the index of the highest similarity score
best_answer_index = np.argmax(similarity_scores)

# Get the best answer
best_answer = answers[best_answer_index]

print("User Question:", user_question)
print("Best Answer:", best_answer)
