from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#loading the gemni model and gemni pro model
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#streamlit
st.set_page_config(page_title="QUESTION & ANSWER")
st.header("Generative LLM Application")

input=st.text_input("Input: ",key="input")
sumbit=st.button("Ask the Question's")
#Resumbit=st.button(" Question's")

#when sumbission
if sumbit:
    response=get_gemini_response(input)
    st.subheader("The Response is --> ")
    st.write(response)