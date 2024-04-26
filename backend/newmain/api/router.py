from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
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