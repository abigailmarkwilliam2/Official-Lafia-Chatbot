import json
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

# Load data from the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)['intents']

# Initialize the 'chat_history' session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Set page configuration
st.set_page_config(page_title="Lafia Chatbot", page_icon=":robot_face:", layout="wide")

# Set background color
page_bg_color = """
<style>
body {
background-color: #darkblue;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Set header styles
header_style = """
<style>
h1 {
    color: #black;
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
    text-align: center;
}
h2 {
    color: #black;
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
    text-align: center;
}
</style>
"""
st.markdown(header_style, unsafe_allow_html=True)

# Display header and subheader
st.markdown("<h1>Welcome to LAFIA:</h1>", unsafe_allow_html=True)
st.markdown("<h2>Your Personal Home Doctor</h2>", unsafe_allow_html=True)

# Set input field styles
input_style = """
<style>
.stTextInput > label {
    color: #4285F4;
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)

input = st.text_input("Input: ", key="input")  # Create a text input field for user input

# Set button styles
button_style = """
<style>
.stButton > button {
    background-color: #blue;
    color: white;
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
    border-radius: 5px;
    padding: 10px 20px;
}
</style>
"""
st.markdown(button_style, unsafe_allow_html=True)

submit = st.button("Ask the question")  # Create a button to submit the user input

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
