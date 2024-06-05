## Conversational Q&A Chatbot with session knowledge
import json
with open('data.json', 'r') as f:
  data = json.load(f)
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI


genai.configure(api_key=os.getenv("AIzaSyCuZS6XSXH8w3CP62I4QlMu_j2pDwq0CMY"))

model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)


st.set_page_config(page_title="Q&A Demo")

st.header("LAFIA")

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="you are a helpfull AI assistant")
    ]

def get_gemini_response(question):
  # Access loaded data (assuming data is a dictionary)
  relevant_info = None
  for key, value in data.items():
    if key.lower() in question.lower():  # Check for keyword match
      relevant_info = value
      break

  # Update conversation history and call model
  # ... (existing code)

  # If relevant info found, use it to enhance response
  if relevant_info:
    response.content += f" (Additional information: {relevant_info})"
  return response
    
