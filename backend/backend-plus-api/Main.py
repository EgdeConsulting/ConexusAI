import fastapi

from easytest import addition
from api.backendai import *
#from backendai import api_query
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/addition")
def read_addition(a: int, b: int):
    return {"result": addition(a, b)}

@app.get("/query", body = {"question": str})
def read_query(question: str):
    return {"result": api_query(question)}
