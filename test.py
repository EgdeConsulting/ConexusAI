import math
from openai import OpenAI
from string import Template

# Initialize OpenAI client
client = OpenAI(api_key="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")

# Function to get embedding vector
def get_embedding_vec(input):
    return client.embeddings.create(
        input=input,
        model="text-embedding-3-large"
    ).data[0].embedding

# Read data from file and create embeddings
with open(r'rawData/quillspike.txt', 'r') as file1:
    lines_from_rawdata = [line.strip() for line in file1.readlines()]

cities = lines_from_rawdata[:]
embeddings = [(city, get_embedding_vec(city)) for city in cities]

def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def get_response(query, embeddings):
    query_embedding = get_embedding_vec(query)

    sorted_result = []
    for city, embedding in embeddings:
        similarity = dot_product(embedding, query_embedding)
        sorted_result.append((city, embedding, similarity))

    sorted_result = sorted(sorted_result, key=lambda x: x[2], reverse=True)

    with open(r'contextTemplates/surfercontext.txt', 'r') as flavor_file:
        flavor_text = flavor_file.read()

    t = Template(f"""
    {flavor_text}
    ===========
    $options
    ===========
    """)

    system_prompt = t.substitute(options="\n\n".join([item[0] for item in sorted_result[:3]]))

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        model="gpt-4-1106-preview"
    )

    print(chat_completion.choices[0].message.content)

# Terminal-based interaction
while True:
    query = input("Enter your query: ")
    if query.lower() == 'exit':
        break
    get_response(query, embeddings)