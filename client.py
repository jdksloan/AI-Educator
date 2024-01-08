from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/category_chain/")
print(remote_chain.invoke({"request": "For lesson 1 can you give me a lesson examples and exercises I can do"}))
