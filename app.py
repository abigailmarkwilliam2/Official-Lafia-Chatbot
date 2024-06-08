import json  # Import the json module to work with JSON data
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv module
load_dotenv()  # Load environment variables from the .env file
import streamlit as st  # Import the Streamlit library for building the web app
import os  # Import the os module for interacting with the operating system


# Load data from the JSON file
with open('data.json', 'r') as f:  # Open the 'data.json' file in read mode
    data = json.load(f)['intents']  # Load the JSON data and access the 'intents' key


# Initialize the 'chat_history' session state if it doesn't exist
if 'chat_history' not in st.session_state:  # Check if 'chat_history' key exists in session state
    st.session_state['chat_history'] = []  # If not, initialize it as an empty list

st.set_page_config(page_title="Lafia Chatbot")  # Set the page title
st.header("Welcome to LAFIA:")  # Display a header
st.subheader("Your Personal Home Doctor")  # Display a subheader

input = st.text_input("Input: ", key="input")  # Create a text input field for user input
submit = st.button("Ask the question")  # Create a button to submit the user input

if submit and input:  # Check if the button is clicked and the input is not empty
    question = input.lower()  # Convert the user input to lowercase
    answer_found = False  # Initialize a flag to track if an answer is found
    for intents in data:  # Loop through each intent in the data
        if any(pattern.lower() in question for pattern in intents['patterns']):  # Check if any pattern matches the user input
            answer = intents['responses'][0]  # Get the first response from the matching intent
            st.subheader("The Response is")  # Display a subheader
            st.write(answer)  # Display the response
            st.session_state['chat_history'].append(("You", input))  # Add the user input to the chat history
            st.session_state['chat_history'].append(("Bot", answer))  # Add the bot response to the chat history
            answer_found = True  # Set the flag to indicate an answer is found
            break  # Exit the loop since an answer is found
    if not answer_found:  # If no answer is found
        st.subheader("The Response is")  # Display a subheader
        st.write("Sorry, I can't answer that directly.")  # Display a default response
        st.session_state['chat_history'].append(("You", input))  # Add the user input to the chat history
        st.session_state['chat_history'].append(("Bot", "Sorry, I can't answer that directly."))  # Add the default response to the chat history



