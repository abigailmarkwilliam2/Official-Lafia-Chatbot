## Conversational Q&A Chatbot with session knowledge and JSON data

from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import json
import google.generativeai as genai
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI


genai.configure(api_key=os.getenv("AIzaSyCuZS6XSXH8w3CP62I4QlMu_j2pDwq0CMY"))

model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)


st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Load data from JSON file (replace 'your_data.json' with your actual filename)
with open('your_data.json', 'r') as f:
  data = json.load(f)

if 'flowmessages' not in st.session_state:
  st.session_state['flowmessages'] = [
      SystemMessage(content="you are a helpful AI assistant")
  ]


def get_gemini_response(question):
  # Check for pre-defined response in JSON data
  if question in data:
    return AIMessage(content=data[question])

  # Access loaded data for additional context (optional)
  relevant_info = None
  for key, value in data.items():
    if key.lower() in question.lower():
      relevant_info = value
      break

  # Update conversation history and call model
  st.session_state['flowmessages'].append(HumanMessage(content=question))
  response = model.invoke(st.session_state['flowmessages'])
  st.session_state['flowmessages'].append(AIMessage(content=response.content))

  # If relevant info found, use it to enhance response (optional)
  if relevant_info:
    response.content += f" (Additional information: {relevant_info})"
  return response


if 'chat_history' not in st.session_state:
  st.session_state['chat_history'] = []


input = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")


if submit and input:
  response = get_gemini_response(question=input)
  st.session_state['chat_history'].append(("You", input))
  st.subheader("The Response is")
  st.write(response.content)
  st.session_state['chat_history'].append(("Bot", response.content))

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
  st.write(f"{role}: {text}")
