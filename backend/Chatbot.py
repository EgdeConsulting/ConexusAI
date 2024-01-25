
from openai import OpenAI
from key import APIkey
import time

client = OpenAI(api_key = APIkey)

#OpenAI.api_key = APIkey

# user query
user_query = input("> ")

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo",
                                               messages = [{"role": "user", 
                                                            "content": user_query}])


#print(chat_completion)

print("")

# prints what you asked
print(f"You asked: {user_query}")
print("")
print("This is the response: ")
print("")

# prints the chat response
print(chat_completion.choices[0].message.content)