import openai, os
from fastapi.encoders import jsonable_encoder as jsonfy
from fastapi import HTTPException
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def openaiMethod(user_message):
    # process input_data
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_message},
            ],
            model="gpt-3.5-turbo",
        )
        answer = chat_completion.choices[0].message.content
        return answer  # Returner kun svaret
    except Exception as e:
        # Løft en HTTPException som FastAPI vil håndtere
        raise HTTPException(status_code=500, detail=f"En feil oppstod: {str(e)}")