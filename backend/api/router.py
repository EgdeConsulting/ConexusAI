from fastapi import APIRouter, Request, HTTPException
from service.testfunc import addition
from service import backendAI, openaiMethod,jsonopenaiMethod
from fastapi.responses import JSONResponse


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

@router.post("/openairoutes/")
async def read_item(request: Request):
    data = await request.json()
    USER_INPUT = data.get("prompt")
    
    # Bruk en try-except blokk for å håndtere potensielle feil
    try:
        answer = openaiMethod(USER_INPUT)
        return JSONResponse(content={"answer": answer}, status_code=200)
    except HTTPException as e:
        # FastAPI vil fange og håndtere HTTPException
        return JSONResponse(content={"error": e.detail}, status_code=e.status_code)

@router.post("/openairoutesss/")
async def read_item(request: Request):
    data = await request.json()
    USER_INPUT = data.get("prompt")
    answer = jsonopenaiMethod(USER_INPUT)
    #function here! 
    #answer = result from query
    return { "answer": answer }