from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate_response")
async def generate_response(prompt: Optional[str] = None):
    if prompt is None:
        return {"error": "No prompt provided"}
    
    # Count the number of letters in the prompt
    num_letters = sum(1 for char in prompt if char.isalpha())
    
    # Construct the response message
    response_message = f"Number of letters = {num_letters}"
    
    # Return the response
    return {"response": response_message}