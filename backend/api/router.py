from service import backendAI, openaiMethod,jsonopenaiMethod, handle_user_query, Config, DatabaseWrapper
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

class QueryResponse(BaseModel):
    sql_query: str
    answer: str
    error: str

router = APIRouter()
class Query(BaseModel):
    prompt: str


@router.post("/queryDBAI/", response_model=QueryResponse)
async def queryAI(query: Query):
    try:
        result = handle_user_query(query.prompt)
        if result["error"]:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except Exception as e:
        # FastAPI vil fange og håndtere generelle unntak
        return {"sql_query": "", "answer": "", "error": str(e)}


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