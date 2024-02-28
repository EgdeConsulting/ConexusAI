import matplotlib.pyplot as plt
import numpy as np
import math
from openai import OpenAI

client = OpenAI (api_key ="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")

def get_embedding_vec(input):
  """Returns the embeddings vector for a given input"""
  return client.embeddings.create(
        input=input,
        model="text-embedding-3-large", # We use the new embeddings model here (announced end of Jan 2024)
        # dimensions=... # You could limit the number of output dimensions with the new embeddings models
    ).data[0].embedding
vec = get_embedding_vec("The OOP conference is awesome")

magnitude = np.linalg.norm(vec)
magnitude

def compare(s):
    sim1 = np.dot(get_embedding_vec(s[0]), get_embedding_vec(s[1]))
    sim2 = np.dot(get_embedding_vec(s[0]), get_embedding_vec(s[2]))
    return (sim1, sim2)



with open(r'C:\Testtemp\TestAPI\rawData\cityinfo.txt','r') as file1:
   lines_from_rawdata = [line.strip() for line in file1.readlines()]

cities = lines_from_rawdata[:]
embeddings = []
for city in cities:
  embeddings.append((city, get_embedding_vec(city)))

query = input("Enter your question: ")

query_embedding = get_embedding_vec(query)

sorted_result = []
for city, embedding in embeddings:
  similarity = np.dot(embedding, query_embedding)
  sorted_result.append((city, embedding, similarity))


sorted_result = sorted(sorted_result, key=lambda x: x[2], reverse=True)
# for tuple in sorted_result:
#     print(tuple[2], tuple[0])

cities = [item[0].split(":", 1)[0] for item in sorted_result]
similarities = [item[2] for item in sorted_result]

plt.bar(cities, similarities, color='lime')
plt.ylabel('Similarity')
plt.ylim(
    math.floor(min(similarities) * 100) / 100,
    math.ceil(max(similarities) * 100) / 100)
plt.xticks(rotation=90)
plt.show()

from string import Template


with open(r'C:\Testtemp\TestAPI\contextTemplates\surfercontext.txt', 'r') as flavor_file:
    flavor_text = flavor_file.read()

# Create a template string
t = Template(f"""
{flavor_text}
===========
$options
===========
""")

system_prompt = t.substitute(options = "\n\n".join([item[0] for item in sorted_result[:3]]))
# print(system_prompt) #Writes to "canvas/setting/instruction"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": query,
        }
    ],
    model="gpt-4-1106-preview",
)
# chat_completion.choices[0].message.content
assistant_reply = chat_completion.choices[0].message.content

# Print the assistant's reply to the screen
print("Assistant's Reply:")
print(assistant_reply)
