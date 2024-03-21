from typing import Optional
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/generate_response")
async def generate_response(prompt: Optional[str] =Body(...)):
    if prompt is None:
        return {"error": "No prompt provided"}
    
    # Count the number of letters in the prompt
    num_letters = sum(1 for char in prompt if char.isalpha())
    
    # Construct the response message
    response_message = f"Number of letters = {num_letters}"
    
    # Return the response
    return {"response": response_message}



@app.post("/reverse_string")
async def reverse_string(text: str = Body(...)):
    reversed_text = text[::-1]
    return {"reversed_text": reversed_text}