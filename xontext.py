import matplotlib.pyplot as plt
import numpy as np
import math
from openai import OpenAI

# def draw_vector(ax, vector, color, label, width=0.01):
#     ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label, width=width)

# # Create subplots
# fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# # Base vector at 45 degrees (π/4), length 1 (normalized)
# base_vector = np.array([np.cos(np.pi/4), np.sin(np.pi/4)])

# # Vectors for cosine similarity calculations
# vectors_sim_1 = [base_vector, base_vector]  # Same as base vector, cosine similarity = 1
# vectors_sim_0 = [base_vector, np.array([-base_vector[1], base_vector[0]])]  # 90 degrees to base vector, cosine similarity = 0
# vectors_sim_neg1 = [base_vector, -base_vector]  # Opposite to base vector, cosine similarity = -1

# # Titles for subplots
# titles = ['Cosine Similarity = 1', 'Cosine Similarity = 0', 'Cosine Similarity = -1']

# # Colors for vectors
# colors = ['blue', 'red']

# # Draw vectors and angles
# for i, ax in enumerate(axs):
#     # Draw the base vector in each subplot
#     draw_vector(ax, base_vector, colors[0], 'Base Vector', 0.02)

#     # Draw the comparison vector depending on the subplot
#     if i == 0:
#         draw_vector(ax, vectors_sim_1[1], colors[1], 'Vector (Sim 1)')
#     elif i == 1:  # Similarity 0
#         draw_vector(ax, vectors_sim_0[1], colors[1], 'Vector (Sim 0)')
#     else:  # Similarity -1
#         draw_vector(ax, vectors_sim_neg1[1], colors[1], 'Vector (Sim -1)')

#     ax.set_xlim(-1.5, 1.5)
#     ax.set_ylim(-1.5, 1.5)
#     ax.axvline(x=0, color='grey', lw=1)
#     ax.axhline(y=0, color='grey', lw=1)
#     ax.set_title(titles[i])
#     ax.legend()

# plt.tight_layout()
# plt.show()

client = OpenAI (api_key ="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")

# def get_embedding_vect(input):
#     return client.embeddings.create(
#         input=input,
#         modek="text-embeddig-3-lagre",
#     ).data[0].embeddig
# Define a helper function to calculate embeddings
def get_embedding_vec(input):
  """Returns the embeddings vector for a given input"""
  return client.embeddings.create(
        input=input,
        model="text-embedding-3-large", # We use the new embeddings model here (announced end of Jan 2024)
        # dimensions=... # You could limit the number of output dimensions with the new embeddings models
    ).data[0].embedding
vec = get_embedding_vec("The OOP conference is awesome")

# print(len(vec)) 
# print(vec[:10])

magnitude = np.linalg.norm(vec)
magnitude

def compare(s):
    sim1 = np.dot(get_embedding_vec(s[0]), get_embedding_vec(s[1]))
    sim2 = np.dot(get_embedding_vec(s[0]), get_embedding_vec(s[2]))
    return (sim1, sim2)

# sentences = [
    # Although sentences 1 and 2 use different words (soccer, football),
    # the cosine similarity of 1 and 2 is higher compared to 1 and 3 because
    # the meaning of 1 and 2 is more similar.
    # ["I enjoy playing soccer on weekends.",
    #  "Football is my favorite sport. Playing it on weekends with friends helps me to relax.",
    #  "In Austria, people often watch soccer on TV on weekends."],

    # Here we test whether the OpenAI embedding model "understands", that the
    # contextual meaning of "Java" is different in sentences 1 and 2. Therefore,
    # the cosine similarity of 1 and 3 is higher as both are programming-related.
    # ["He is interested in Java programming.",
    #  "He visited Java last summer.",
    #  "He recently started learning Python programming."],

    # The next example deals with negation handling. All three sentences are
    # about whether someone likes going to the gym. Sentences 1 and 3 are positive
    # (i.e. like training in the gym), while 2 is not. Therefore, 1 and 3 have
    # a higher cosine similarity.
    # ["I like going to the gym.",
    #  "I don't like going to the gym.",
    #  "I don't dislike going to the gym."],

    # Let's take a look at ideomatic expressions. Sentences 1 and 2 have very
    # similar meaning. 3 also contains "cats and dogs", but the meaning is different.
    # As a result, cosine similarity between 1 and 2 is higher.
    # ["It's raining cats and dogs.",
    #  "The weather is very bad, it's pouring outside.",
    #  "Cats and dogs don't go outside when it rains."],

    # The next examples demonstrate that embedding models have been pre-trained
    # with data about the real world. They understand certain domain-specific terms
    # like "virus" and "Voron".
    # ["The computer was infected with a virus.",
    #  "The patient's viral load is detectable.",
    #  "She is updating the antivirus software on her laptop."],
    # ["I need to get better slicing skills to make the most of my Voron.",
    #  "3D printing is a worth-while hobby.",
    #  "Can I have a slice of bread?"],

    # The last example demonstrates the limits of embeddings. Berry Harris is
    # a well-known teacher in Jazz. Using "the 6th on the 5th" is typical for him.
    # One must know Berry Harris and the musical theory that he has tought to
    # understand the similarity of the sentences 1 and 2. OpenAI embeddings
    # do not understand that.
#     ["I like how Barry Harris described Jazz theory.",
#      "Playing the 6th on the 5th is an important concept that you must understand.",
#      "My friends Barry and Harris often visit me to play computer games."]
# ]
# print(f"Semantic similarity: {compare(sentences[0])}")
# print(f"Contextual meaning: {compare(sentences[1])}")
# print(f"Negation handling: {compare(sentences[2])}")
# print(f"Idiomatic expressions: {compare(sentences[3])}")
# print(f"Domain-specific language (1): {compare(sentences[4])}")
# print(f"Domain-specific language (2): {compare(sentences[5])}")
# print(f"Domain-specific language (3): {compare(sentences[6])}")


# Array with descriptions about cities. They could be used in e.g. a travel
# agency to find suitable spots for vacations
cities = []
cities.append("Emeraldine: A bustling metropolis surrounded by lush forests, known for its towering skyscrapers and vibrant night markets.")
cities.append("Solara: A small, sun-drenched coastal town famous for its golden beaches, seafood cuisine, and laid-back lifestyle.")
cities.append("Nebulae: A futuristic city with floating buildings and neon lights, renowned for its advanced technology and AI-driven services.")
cities.append("Auroria: A serene mountain city, hidden in misty peaks, with ancient monasteries and breathtaking hiking trails.")
cities.append("Thalassa: An island city with a rich maritime history, surrounded by crystal clear waters, perfect for scuba diving and sailing.")
cities.append("Cinderpeak: A city built around an active volcano, known for its unique architecture, geothermal energy, and vibrant arts scene.")
cities.append("Vespera: A city that never sleeps, with a bustling nightlife, cultural festivals, and a diverse culinary scene, under a starlit sky.")
cities.append("Windmere: A small town on the plains, famous for its windmills, open fields, and a tight-knit community with traditional values.")
cities.append("Polaria: An isolated city in the far north, known for its ice castles, aurora borealis views, and resilient, warm-hearted residents.")
cities.append("Glimmerdale: A city in a valley, illuminated by bioluminescent plants, known for its sustainable living and harmony with nature.")


# Let's calculate the embedding vectors of all cities.
# Here we simply store them in an array in memory.
embeddings = []
for city in cities:
  embeddings.append((city, get_embedding_vec(city)))


 # Enter the search text of the customer how is looking for a vacation spot.
#query = "For vacation, I want to go hiking in the mountains. I want to really feel nature."
#query = "In my vacation, I want to party, party, party!"
#query = "I want to travel to an underwater city"
#query = "What is the name of Bart Simpson's sister?"
query = input("Enter your question: ")
# Calculate the embedding vector of the search text
query_embedding = get_embedding_vec(query)


sorted_result = []

# Iterate over all cities and calculate the similarity (dot product) of
# the city description and the search text.
for city, embedding in embeddings:
  similarity = np.dot(embedding, query_embedding)
  sorted_result.append((city, embedding, similarity))

# We sort the result descending based on the similarity so that the top
# elements are probably more relevant than the last ones.
sorted_result = sorted(sorted_result, key=lambda x: x[2], reverse=True)
for tuple in sorted_result:
    print(tuple[2], tuple[0])

cities = [item[0].split(":", 1)[0] for item in sorted_result]
similarities = [item[2] for item in sorted_result]

# Visualize the sorted result in a bar chart
plt.bar(cities, similarities, color='lime')
plt.ylabel('Similarity')
plt.ylim(
    math.floor(min(similarities) * 100) / 100,
    math.ceil(max(similarities) * 100) / 100)
plt.xticks(rotation=90)
plt.show()


from string import Template

t = Template("""
You are a helpful assistant in a travel agency. Customers are describing
what they want to do in their vacation. Make suggestions based on the
city descriptions provided below. ONLY use the provided city descriptions.
Do NOT use other information sources.

If you cannot generate a meaningful answer based on the given city description,
say "Sorry, I cannot help". If the user's input is not related to finding
a travel location, say "Sorry, I can only help with vacation locations".

===========
$options
===========
""")

system_prompt = t.substitute(options = "\n\n".join([item[0] for item in sorted_result[:3]]))
print(system_prompt)

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
chat_completion.choices[0].message.content
