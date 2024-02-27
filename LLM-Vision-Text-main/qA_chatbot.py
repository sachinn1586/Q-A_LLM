from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
## function 

model=genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response
st.set_page_config(page_title="Q&A Demo")
st.header("LLM Application for the Q&A ")

#Initialize session state for chat history if it does not exits
if 'chat_History' not in st.session_state:
    st.session_state['chat_History']= []

input=st.text_input("Input:",key="input")
sumbit=st.button("ASK the Question")    
    
if sumbit and input:
    response=get_gemini_response(input)
    
    ##ADD users query and response to session chat history
    st.session_state['chat_History'].append(("you",input))
    st.subheader("the Response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_History'].append(("bot",chunk.text))
        
st.header(" this chat History in ")

for role,text in st.session_state['chat_History']:
    st.write(f"{role}:{text}")
