from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def read_item():
    return {"Hello": "World"}   

@app.get("/hello/{name}")
async def read_item(name):
    return {"Hello": name}

@app.get("/query/{query}")
async def read_item(query):
    return {"Query": query}

@app.get("/reverse")
async def reverse_string(query_param: str):
    reversed_string = query_param[::-1]
    return {"reversed_string": reversed_string}

