import fastapi

from easytest import EasyTest

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
