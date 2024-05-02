from fastapi import FastAPI
from api.router import router
#import sys

app = FastAPI()

app.include_router(router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app",  host="0.0.0.0", port=80, reload=True)