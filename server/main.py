from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langserve import add_routes
from dotenv import dotenv_values

secrets = dotenv_values(".env")
secret = secrets["API_KEY"]

# 1. Chain definition
template = """You are a helpful language tutor who asses language levels by providing detailed level breakdowns in 
Common European Framework of Reference (CEFR). The user will ask for a language assessment and provide the target 
langauge. You will ask the user five languages questions to create your assessment, then provide a breakdown and 
score of their level"""
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
