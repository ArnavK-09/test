from transformers import BertTokenizer, BertForQuestionAnswering
import torch

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

# Load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForQuestionAnswering.from_pretrained(model_name)

# User input
user_input = input("Ask:- ")

# Tokenize user input and question
input_ids = tokenizer.encode(user_input, questions[0], add_special_tokens=True)
input_ids = torch.tensor(input_ids).unsqueeze(0)  # Batch dimension

# Get model's predicted answer
outputs = model(input_ids)
start_scores = outputs.start_logits
end_scores = outputs.end_logits

start_index = torch.argmax(start_scores)
end_index = torch.argmax(end_scores) + 1  # Add 1 to include the end index

# Decode the answer from token IDs
answer = tokenizer.decode(input_ids[0][start_index:end_index])

print("User Input:", user_input)
print("Answer:", answer)
