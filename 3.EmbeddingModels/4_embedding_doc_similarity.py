from typing import Any


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2", dimensions=300)

docs = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Bangalore is the IT capital of India"
]

query = "What is the capital of India?"

docs_embedding = embedding.embed_documents(docs)
query_embedding = embedding.embed_query(query)

similarity = cosine_similarity([query_embedding], docs_embedding)[0]
index, score = (sorted(list(enumerate(similarity)), key=lambda x: x[1])[-1])

print(docs[index])
print("Similarity Score ", score)
