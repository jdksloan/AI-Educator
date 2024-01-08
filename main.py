from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langserve import add_routes
from dotenv import dotenv_values

secrets = dotenv_values(".env")
secret = secrets["API_KEY"]

# 1. Chain definition


template = """You are a helpful English language tutor who creates language courses with detailed lesson breakdowns 
based on the length given. A user will pass in a course request with a time frame and you need to create a course 
with a per lesson breakdown"""
human_template = "{request}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])
category_chain = chat_prompt | ChatOpenAI(openai_api_key=secret) | StrOutputParser()

# 2. App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

# 3. Adding chain route
add_routes(
    app,
    category_chain,
    path="/category_chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
