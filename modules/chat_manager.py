from datetime import datetime

import streamlit as st


def init_messages():
    if "messages" not in st.session_state:
        st.session_state.messages = []


def clear_messages():
    st.session_state.messages = []


def add_message(role: str, content: str, sources=None):
    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "sources": sources,
        }
    )


def build_chat_history() -> str:
    history = ""
    for message in st.session_state.messages:
        history += (
            f'{message["role"].capitalize()}: '
            f'{message["content"]}\n'
        )
    return history


def format_timestamp(iso_timestamp: str) -> str:
    if not iso_timestamp:
        return ""
    return datetime.fromisoformat(iso_timestamp).strftime("%b %d, %Y · %I:%M %p")


def render_source_chunks(chunks):
    with st.expander("📚 Source Chunks", expanded=False):
        for i, chunk in enumerate(chunks):
            st.markdown(f"**Chunk {i + 1}**")
            st.markdown(chunk)
            if i < len(chunks) - 1:
                st.divider()


def render_chat_history():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            # Timestamp
            timestamp = message.get("timestamp", "")

            if timestamp:
                st.caption(f"🕒 {format_timestamp(timestamp)}")

            # Message
            st.write(message["content"])

            # Sources
            if (
                message["role"] == "assistant"
                and message.get("sources")
            ):

                with st.expander("📚 View Retrieved Sources"):
                    render_source_chunks(message["sources"])