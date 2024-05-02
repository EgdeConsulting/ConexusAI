from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from test_old_version_new_query_final_a_only import get_input_from_frontend
from openAI_method import openaiMethod
from test_old_version_new_query_final_a_only import get_input_from_frontend
router = APIRouter()

@router.get("/")
async def read_root():
    message = "ConexisAI"
    docs_url = "/docs'>"
    return {"message": message}

@router.post("/message/")
async def read_item(request: Request):
    data = await request.json()
    query = data.get("prompt")
    answer = get_input_from_frontend(query)
    return { "output": answer}

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
    
@router.post("/message/")
async def read_item(request: Request):
    data = await request.json()
    USER_INPUT = data.get("prompt")
    answer = get_input_from_frontend(USER_INPUT)
    
    return { "output": answer }
    