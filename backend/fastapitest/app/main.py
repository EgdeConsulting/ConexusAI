from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def read_item():
    return {"Hello": "World"}   
@app.get("/hello/{name}")
async def read_item(name):
    return {"Hello": name}

