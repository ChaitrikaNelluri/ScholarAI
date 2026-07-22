import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

COLLECTION_NAME = "scholarai_collection"


def retrieve_relevant_chunks(question, top_k=3):

    collection = client.get_collection(COLLECTION_NAME)

    embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results["documents"][0]