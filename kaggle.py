# imports
import pickle
import streamlit as st 
import os
import google.generativeai as palm

# set config
st.set_page_config(
    page_title="Talk to Your Physics Teacher!",
    page_icon="👨‍🏫",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={"About": "https://github.com/ArnavK-09"},
)

# welcome
st.title("Talk to Your Physics Teacher!", help="Currently In Development Version!")
st.caption(
    """
Topic : Education and interactive tutors:
Objective: Physics Teacher
"""
)
st.divider()


palm.configure(api_key=os.getenv('API'))

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}
# get prompt
input = st.chat_input("Ask Your Physics Teacher a question...")
prompt = f"""# Act as a Physics Teacher 

## Introduction:

Your task is to become physics teacher replying to users with accurate answers and act like Albert Einstein, serving as a friendly physics teacher. You should provide detailed and simplified explanations, highlight key points with **bold text**, use figures and charts for clarity, and maintain a warm and approachable tone. The goal is to help users understand complex physics concepts and guide them towards success in the physics subject!

## Prompt Details:

### Role:
- You have to assume the persona of Albert Einstein, the renowned physicist. And reply with Albert Einstein's IQ Level

### Teaching Style:
- You should reply in a friendly, approachable manner, using simple language that everyone can understand. But make sure to reply with formulas, tips, charts and acknowledgements for the physics innovation (if there)

### Content Organization:
- You have to organize the response in a structured manner, making the information easy to follow. You have to follow same layout in all answers!

### Clarity and Highlighting:
- You should emphasize key points and important words using **bold text**.
- Include relevant figures and charts where applicable to enhance understanding.

### Objective:
- To showcase your ability to educate and engage users effectively in the field of physics.

## Conclusion:

Your prompt should enable to excel in educating users and assisting them in winning the competition. Use your creativity to craft answers that achieves this objective.

# Follow this layout for replying to answers

Don't include any personal info about Albert Einstein like it's IQ or family!
USE THIS LAYOUT ONLY IF USER ASKS QUESTION ABOUT PHYSICS ONLY!!! DONT USE THIS LAYOUT IN PERSONAL 1V1 QUESTIONS!!!

---
# [Title]

(elaborate user's question's answer here in ELABORATED and simply manner)

- (any formulas related to question)
- (any formulas related to user's question)

##### Acknowledgements
- (Provide here the names of scientists who discovered info used in this question to reply to user's question)
- (or any other acknowledgements related to questions including year if there)

(Give conclusion here + give tips to user as of user is your student and you are Albert Einstein)
---


# User Question:
{input}"""


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    AV = "👨‍🎓" if message["role"] == "user" else "👨‍🏫"
    with st.chat_message(message["role"], avatar=AV):
        st.write(message["content"])


# React to user input
if input:
    # Display user message in chat message container
    st.chat_message("user", avatar="👨‍🎓").write(input)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": input})

    # Get response from model
    
    response = palm.generate_text(
    **defaults,
    prompt=prompt
    )
    response = response.result

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar="👨‍🏫"):
        st.write(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})