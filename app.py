import json  # Import the json module to work with JSON data
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv module
load_dotenv()  # Load environment variables from the .env file
import streamlit as st  # Import the Streamlit library for building web apps
import os  # Import the os module to interact with the operating system
import google.generativeai as genai  # Import the generativeai module from the Google Cloud AI library
from langchain.schema import HumanMessage, SystemMessage, AIMessage  # Import message classes from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI  # Import the ChatGoogleGenerativeAI class from LangChain


# Configure the Google Generative AI API with the API key from the environment variable
genai.configure(api_key=os.getenv("AIzaSyCuZS6XSXH8w3CP62I4QlMu_j2pDwq0CMY"))

# Create an instance of the ChatGoogleGenerativeAI model with the specified configuration
model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)


st.set_page_config(page_title="Lafia Chatbot")  # Set the page title for the Streamlit app

st.header("Welcome to LAFIA:")  # Display a header with the text "LAFIA:"
st.subheader("Your Personal Home Doctor") # add a sub-header 

# Load data from a JSON file (replace 'your_data.json' with your actual filename)
with open('data.json', 'r') as f:
  data = json.load(f)

# Initialize the 'flowmessages' session state with a system message
if 'flowmessages' not in st.session_state:
  st.session_state['flowmessages'] = [
    SystemMessage(content="you are a helpful AI assistant")
  ]


def get_gemini_response(question):  # Corrected function name
  # Check for pre-defined answer in JSON data
  for item in data:
    if question.lower() in item.get('patterns', []):
      answer = item.get('responses', 'Sorry, I can\'t answer that directly.')
      return AIMessage(content=answer)

  # Fallback to Gemini model if no direct answer found
  st.session_state['flowmessages'].append(HumanMessage(content=question))
  response = model.invoke(st.session_state['flowmessages'])  # Use response instead of answeres
  st.session_state['flowmessages'].append(AIMessage(content=response.content))
  return response


# Initialize the 'chat_history' session state if it doesn't exist
if 'chat_history' not in st.session_state:
  st.session_state['chat_history'] = []


input = st.text_input("Input: ", key="input")  # Create a text input field for user input

submit = st.button("Ask the question")  # Create a button to submit the user input


if submit and input:
  response = get_gemini_response(input)  # Use response instead of answeres
  st.session_state['chat_history'].append(("You", input))  # Add the user input to the chat history
  st.subheader("The Response is")  # Corrected typo
  # Optionally, display a label indicating the source of the answer
  if response.content in [item.get('responses', []) for item in data]:
    st.write(f"Pre-defined Answer: {response.content}")  # Display a label for pre-defined answers
  else:
    st.write(response.content)  # Display the response from the Gemini model
  st.session_state['chat_history'].append(("Bot", response))  # Add the bot's response to the chat history
