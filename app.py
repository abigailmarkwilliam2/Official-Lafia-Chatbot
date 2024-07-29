import json  # Import the json module to work with JSON data
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv module
load_dotenv()  # Load environment variables from the .env file
import streamlit as st  # Import the Streamlit library for building the web app

# Load data from the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)['intents']  # Load the JSON data and access the 'intents' key

# Initialize the 'chat_history' session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []  # If not, initialize it as an empty list

# Set page config with a custom favicon (optional)
st.set_page_config(
    page_title="Lafia Chatbot",
    page_icon="path/to/your/favicon.ico",  # Replace with path to your favicon
)

# Container for the header and subheader (improves layout)
header_container = st.container()

with header_container:
    st.header("Welcome to LAFIA:")  # Display a header
    st.subheader("Your Personal Home Doctor")  # Display a subheader

# Create columns for input and chat history (improves layout)
input_col, history_col = st.columns(2)

# Text input field with a placeholder
with input_col:
    input = st.text_input("Ask Lafia anything...", key="input")

# Submit button with a different style
with input_col:
    submit = st.button("Ask", key="submit", style="background-color: #007bff; color: white;")

if submit and input:
    question = input.lower()  # Convert the user input to lowercase
    answer_found = False  # Initialize a flag to track if an answer is found

    for intents in data:
        if any(pattern.lower() in question for pattern in intents['patterns']):
            answer = intents['responses'][0]  # Get the first response from the matching intent

            # Container for response and chat history (improves layout)
            response_container = st.container()

            with response_container:
                st.subheader("Lafiya Says:")  # Display a subheader in a container
                st.write(answer)  # Display the response

            st.session_state['chat_history'].append(("You", input))  # Add user input to chat history
            st.session_state['chat_history'].append(("Bot", answer))  # Add bot response to chat history
            answer_found = True
            break

    if not answer_found:
        with response_container:
            st.subheader("Lafiya Says:")  # Display a subheader in the same container
            st.write("Sorry, I can't answer that directly.")  # Display a default response

        st.session_state['chat_history'].append(("You", input))  # Add user input to chat history
        st.session_state['chat_history'].append(("Bot", "Sorry, I can't answer that directly."))  # Add default response to chat history
