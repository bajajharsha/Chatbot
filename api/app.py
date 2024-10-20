from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes                # responsibe for making apis
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

prompt=ChatPromptTemplate.from_template("Write me a poem about {topic} in 100 words")
llm = Ollama(model="llama2")

add_routes(
    app,
    prompt|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)