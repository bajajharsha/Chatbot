import requests
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

def get_llama2_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", json={"input": {"topic":input_text}}) 
    return response.json()["output"]

st.title('Langchain API Demo(langserve)')
input_text=st.text_input("Generate the poem that you want")

if input_text:
    st.write(get_llama2_response(input_text))