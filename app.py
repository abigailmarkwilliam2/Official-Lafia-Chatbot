import json
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI


genai.configure(api_key=os.getenv("AIzaSyCuZS6XSXH8w3CP62I4QlMu_j2pDwq0CMY"))

model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)


st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Load data from JSON file (replace 'your_data.json' with your actual filename)
with open('data.json', 'r') as f:
  data = json.load(f)

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


