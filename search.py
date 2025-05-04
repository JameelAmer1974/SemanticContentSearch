from dotenv import load_dotenv
from pprint import pprint
import requests
import os
#from database_connection import save_document
from doc_embeddings import get_doc_embedding
#from sentence_transformers import SentenceTransformer
from postgres_connection import  cosine_similarity_search

if __name__ == '__main__':

    # Query text
    query_text = ("الحرب في سوريا")
    query_embedding = get_doc_embedding(query_text).tolist()
    results = cosine_similarity_search(query_embedding)
    for text, similarity in results:
        print(f"📌 Match: {text} | 🔥 Similarity: {similarity:.4f}")
