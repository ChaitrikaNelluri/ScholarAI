# ==========================
# ScholarAI Configuration
# ==========================

# Text Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Embedding Model
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# Gemini Model
LLM_MODEL = "gemini-2.5-flash"

# ChromaDB
CHROMA_DB_PATH = "chroma_db"
COLLECTION_NAME = "scholarai_collection"

# Retriever
TOP_K_RESULTS = 3