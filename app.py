import json
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os

# Load data from the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)['intents']

# Initialize the 'chat_history' session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

st.set_page_config(page_title="Lafia Chatbot")
st.header("Welcome to LAFIA:")
st.subheader("Your Personal Home Doctor")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    question = input.lower()
    answer_found = False
    for intent in data:
        if any(pattern.lower() in question for pattern in intent['patterns']):
            answer = intent['responses'][0]
            st.subheader("The Response is")
            st.write(answer)
            st.session_state['chat_history'].append(("You", input))
            st.session_state['chat_history'].append(("Bot", answer))
            answer_found = True
            break
    if not answer_found:
        st.subheader("The Response is")
        st.write("Sorry, I can't answer that directly.")
        st.session_state['chat_history'].append(("You", input))
        st.session_state['chat_history'].append(("Bot", "Sorry, I can't answer that directly."))
