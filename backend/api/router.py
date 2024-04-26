from fastapi import APIRouter, Request, HTTPException
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
"""
@router.post("/openairoutesss/")
async def read_item(request: Request):
    data = await request.json()
    query = data.get("prompt")
    answer = get_input_from_frontend(query)
    #answer = result from query
    return { "answer": answer }"""