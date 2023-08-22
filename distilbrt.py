from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

tokenizer = DistilBertTokenizer.from_pretrained(
    'distilbert-base-uncased', return_token_type_ids=True)
model = DistilBertForQuestionAnswering.from_pretrained(
    'distilbert-base-uncased-distilled-squad')


context = """
in recent years, advancements in artificial intelligence have led to remarkable breakthroughs in various fields. Natural language processing (NLP), a branch of AI, focuses on enabling machines to understand, interpret, and generate human language. This has paved the way for applications like chatbots, language translation, and sentiment analysis. One of the notable achievements is the development of transformer-based models like GPT-3, which can generate coherent and contextually relevant text by predicting the next word in a sequence. These models have demonstrated impressive language generation capabilities and are being used in content creation, virtual assistants, and even coding assistance.
"""

question = input("Ask -> ")

encoding = tokenizer.encode_plus(question, context)


input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

start_scores, end_scores = model(torch.tensor(
    [input_ids]), attention_mask=torch.tensor([attention_mask]),return_dict=False)

ans_tokens = input_ids[torch.argmax(start_scores): torch.argmax(end_scores)+1]
answer_tokens = tokenizer.convert_ids_to_tokens(
    ans_tokens, skip_special_tokens=True)

print("\nQuestion ", question)
print("\nAnswer Tokens: ")
print(answer_tokens)

answer_tokens_to_string = tokenizer.convert_tokens_to_string(answer_tokens)

print("\nAnswer : ", answer_tokens_to_string)
