from fastapi import APIRouter
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

@router.get("/test/{input_int1}{input_int2}")
async def test(input_int1: int, input_int2: int):
    result =addition(input_int1, input_int2)
    return {"result": result}   
