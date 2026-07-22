import chromadb
import streamlit as st

from config import CHROMA_DB_PATH, COLLECTION_NAME
from modules.embeddings import generate_embeddings
from modules.pdf_reader import extract_text_from_pdf
from modules.text_chunker import split_text_into_chunks
from modules.vector_store import store_embeddings


def init_document_state():
    if "documents" not in st.session_state:
        st.session_state.documents = []
    if "all_chunks" not in st.session_state:
        st.session_state.all_chunks = []
    if "processed_files" not in st.session_state:
        st.session_state.processed_files = set()
    if "total_embeddings" not in st.session_state:
        st.session_state.total_embeddings = 0
    if "embedding_dimensions" not in st.session_state:
        st.session_state.embedding_dimensions = 0


def _file_key(uploaded_file):
    return f"{uploaded_file.name}_{uploaded_file.size}"


def has_documents():
    return len(st.session_state.get("all_chunks", [])) > 0


def get_chroma_chunk_count():
    try:
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        collection = client.get_collection(COLLECTION_NAME)
        return collection.count()
    except Exception:
        return 0


def process_uploads(uploaded_files):
    if not uploaded_files:
        return 0

    new_count = 0

    for uploaded_file in uploaded_files:
        key = _file_key(uploaded_file)
        if key in st.session_state.processed_files:
            continue

        text = extract_text_from_pdf(uploaded_file)
        chunks = split_text_into_chunks(text)

        if not chunks:
            st.warning(f"'{uploaded_file.name}' produced no text chunks.")
            continue

        st.session_state.all_chunks.extend(chunks)
        st.session_state.documents.append(
            {
                "name": uploaded_file.name,
                "chunks": len(chunks),
            }
        )
        st.session_state.processed_files.add(key)
        new_count += 1

    if new_count == 0:
        return 0

    embeddings = generate_embeddings(st.session_state.all_chunks)
    store_embeddings(st.session_state.all_chunks, embeddings)

    st.session_state.total_embeddings = len(embeddings)
    st.session_state.embedding_dimensions = (
        len(embeddings[0]) if len(embeddings) > 0 else 0
    )

    return new_count


def clear_database():
    try:
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        for collection in client.list_collections():
            if collection.name == COLLECTION_NAME:
                client.delete_collection(COLLECTION_NAME)
                break
    except Exception:
        pass

    st.session_state.documents = []
    st.session_state.all_chunks = []
    st.session_state.processed_files = set()
    st.session_state.total_embeddings = 0
    st.session_state.embedding_dimensions = 0


def get_stats():
    return {
        "total_files": len(st.session_state.documents),
        "total_chunks": len(st.session_state.all_chunks),
        "total_embeddings": st.session_state.total_embeddings,
        "chroma_count": get_chroma_chunk_count(),
    }
