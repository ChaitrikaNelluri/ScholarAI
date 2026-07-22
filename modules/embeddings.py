from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

# Load the embedding model only once
model = SentenceTransformer(EMBEDDING_MODEL)


def generate_embeddings(chunks):

    embeddings = model.encode(chunks)

    return embeddings