import chromadb

COLLECTION_NAME = "scholarai_collection"

client = chromadb.PersistentClient(path="chroma_db")


def store_embeddings(chunks, embeddings):

    # Delete old collection
    collections = client.list_collections()

    for collection in collections:
        if collection.name == COLLECTION_NAME:
            client.delete_collection(COLLECTION_NAME)
            break

    # Create new collection
    collection = client.create_collection(
        name=COLLECTION_NAME
    )

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    print(f"Stored {len(chunks)} chunks.")