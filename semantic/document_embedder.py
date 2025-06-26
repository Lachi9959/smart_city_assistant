
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import pinecone

load_dotenv()
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="us-west1-gcp")
index = pinecone.Index("smartcity-index")
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_documents(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        vector = model.encode(line).tolist()
        index.upsert([(f"line-{i}", vector, {"text": line})])
