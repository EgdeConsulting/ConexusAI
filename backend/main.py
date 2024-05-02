from fastapi import FastAPI
from api.router import router
import sys

app = FastAPI()

app.include_router(router)