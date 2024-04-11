from fastapi import APIRouter, Request
from service.testfunc import addition


router = APIRouter()


@router.get("/")
async def read_root():
    message = "ConexisAI"
    docs_url = "/docs'>"
    return {"message": message}

@router.get("/query/{input_string}")
async def read_item(input_string: str):
    return {"input_string": input_string}

@router.post("/message/")
async def read_item(request: Request):
    data = await request.json()
    USER_INPUT = data.get("prompt")
    #function here! 
    #answer = result from query
    return { "answer": "placeholder" }

@router.get("/test/")
async def test(input_int1: int, input_int2: int):
    result =addition(input_int1, input_int2)
    return {"result": result}   
