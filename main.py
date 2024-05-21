import os 
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama 

import streamlit as st


load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")

prompt  = ChatPromptTemplate.from_messages(
    [
        ("system","You are a master coder, help others to solve their coding problems"),
        ("user","Question:{question}"),
    ]
)

st.title("Langchain with Codelama")
input_text = st.text_input("make me helpfull")

llm = Ollama(model="codellama")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))



