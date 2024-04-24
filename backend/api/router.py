from service import backendAI, openaiMethod,jsonopenaiMethod
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from service import handle_user_query  


router = APIRouter()

@router.post("/query/")
async def query(prompt: str):
    try:
        # Kaller handle_user_query-funksjonen fra query_handler med brukerens prompt
        answer = handle_user_query(prompt)
        return JSONResponse(content={"answer": answer}, status_code=200)
    except Exception as e:
        # FastAPI vil fange og håndtere generelle unntak
        return JSONResponse(content={"error": str(e)}, status_code=500)


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

@router.post("/openairoutesss/")
async def read_item(request: Request):
    data = await request.json()
    USER_INPUT = data.get("prompt")
    answer = jsonopenaiMethod(USER_INPUT)
    #function here! 
    #answer = result from query
    return { "answer": answer }