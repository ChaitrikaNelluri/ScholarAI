
import importlib
import inspect

import streamlit as st

from modules.chat_manager import (
    add_message,
    build_chat_history,
    clear_messages,
    init_messages,
    render_chat_history,
)

from modules.document_manager import (
    clear_database,
    get_stats,
    has_documents,
    init_document_state,
    process_uploads,
)

from modules.voice_assistant import (
    speech_to_text,
    text_to_speech,
)

from modules.mindmap import (
    generate_mindmap,
)

from modules.study_planner import (
    generate_study_plan,
)

import modules.gemini_llm as _gemini_llm

from modules.retriever import (
    retrieve_relevant_chunks,
)

# Always reload the latest gemini_llm module
importlib.reload(_gemini_llm)

generate_answer = _gemini_llm.generate_answer
get_summary = _gemini_llm.get_summary
get_study_notes = _gemini_llm.get_study_notes
get_key_points = _gemini_llm.get_key_points
get_quiz = _gemini_llm.get_quiz
get_flashcards = _gemini_llm.get_flashcards
get_mindmap = _gemini_llm.get_mindmap
get_study_plan = _gemini_llm.get_study_plan


def configure_page():

    st.set_page_config(
        page_title="ScholarAI",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ===============================
       MAIN APP
    =============================== */

    .stApp{
        background:#2A211C;
        color:#F8F3EB;
        font-family:'Inter',sans-serif;
    }

    html, body, [class*="css"]{
        background:#2A211C;
        color:#F8F3EB;
        font-family:'Inter',sans-serif;
    }

    /* ===============================
       SIDEBAR
    =============================== */

    section[data-testid="stSidebar"]{
        background:#352922;
        border-right:1px solid #5A4639;
    }

    section[data-testid="stSidebar"] *{
        color:#F8F3EB !important;
    }

    /* =====================================
   SIDEBAR COLLAPSE BUTTON
===================================== */

button[kind="header"]{
    color:#FFFFFF !important;
    background:transparent !important;
}

button[kind="header"] svg{
    fill:#FFFFFF !important;
    color:#FFFFFF !important;
}

button[kind="header"]:hover{
    background:#4A392F !important;
}

button[kind="header"]:hover svg{
    fill:#D6B98C !important;
}
    /* ===============================
       TEXT
    =============================== */

    h1,h2,h3,h4,h5,h6{
        color:#F8F3EB !important;
        font-weight:700;
    }

    p,
    label,
    span,
    small,
    li,
    div{
        color:#F8F3EB !important;
    }

    [data-testid="stMarkdownContainer"]{
        color:#F8F3EB !important;
    }

    /* ===============================
       BUTTONS
    =============================== */

    .stButton > button{

        background:#D6B98C;
        color:#2A211C !important;

        border:none;

        border-radius:14px;

        font-weight:700;

        padding:12px 22px;

        transition:0.3s;

        box-shadow:0 5px 15px rgba(0,0,0,.35);

    }

    .stButton > button:hover{

        background:#E5CDA7;

        color:#2A211C !important;

        transform:translateY(-2px);

    }

    /* ===============================
       CHAT MESSAGES
    =============================== */

    div[data-testid="stChatMessage"]{

        background:#3A2D25;

        color:#F8F3EB;

        border-radius:18px;

        border:1px solid #5C4A3F;

        padding:18px;

        margin-bottom:15px;

        box-shadow:0 5px 15px rgba(0,0,0,.25);

    }

    /* ===============================
       METRIC CARDS
    =============================== */

    div[data-testid="metric-container"]{

        background:#3A2D25;

        border-radius:18px;

        border:1px solid #5C4A3F;

        padding:18px;

        color:#F8F3EB;

    }

    /* =====================================
     FILE UPLOADER TEXT
    ===================================== */

   /* Upload button text */
      section[data-testid="stFileUploader"] button p{
      color:#2A211C !important;
}

   /* "Upload" text */
      section[data-testid="stFileUploader"] p{
      color:#333333 !important;
}

   /* "200MB per file • PDF" */
    section[data-testid="stFileUploader"] small{
    color:#333333 !important;
    opacity:1 !important;
}

   /* Some Streamlit versions use span instead of small */
    section[data-testid="stFileUploader"] span{
    color:#F8F3EB !important;
}

    /* Drag & Drop text */
    section[data-testid="stFileUploader"] label{
    color:#F8F3EB !important;
    }

    /* ===============================
       INPUT BOX
    =============================== */

    textarea{

        background:#3A2D25 !important;

        color:#F8F3EB !important;

        border:1px solid #5C4A3F !important;

        border-radius:18px !important;

    }

    input{

        background:#3A2D25 !important;

        color:#F8F3EB !important;

    }

    textarea::placeholder,
    input::placeholder{

        color:#D8C9B5 !important;

        opacity:1;

    }

    /* ===============================
       TABS
    =============================== */

    button[data-baseweb="tab"]{

        background:#3A2D25;

        color:#F8F3EB !important;

        border-radius:14px;

        border:1px solid #5C4A3F;

        padding:10px 18px;

        font-weight:600;

    }

    button[data-baseweb="tab"]:hover{

        background:#4A392F;

    }

    button[aria-selected="true"]{

        background:#D6B98C !important;

        color:#2A211C !important;

        font-weight:700;

    }

    /* ===============================
       ALERT BOXES
    =============================== */

    div[data-testid="stAlert"]{

        background:#3A2D25;

        color:#F8F3EB;

        border-radius:15px;

    }

    /* ===============================
       SCROLLBAR
    =============================== */

    ::-webkit-scrollbar{

        width:10px;

    }

    ::-webkit-scrollbar-track{

        background:#2A211C;

    }

    ::-webkit-scrollbar-thumb{

        background:#B89568;

        border-radius:20px;

    }

    ::-webkit-scrollbar-thumb:hover{

        background:#D6B98C;

    }

    </style>
    """, unsafe_allow_html=True)


def render_sidebar():

    with st.sidebar:

        # ==========================================
        # LOGO
        # ==========================================

        st.title("📚 ScholarAI")
        st.caption("Research • Learn • Master")

        st.divider()

        # ==========================================
        # UPLOAD
        # ==========================================

        st.subheader("📂 Upload Documents")

        uploaded_files = st.file_uploader(
            "Choose PDF Files",
            type=["pdf"],
            accept_multiple_files=True,
            label_visibility="collapsed",
        )

        if uploaded_files:

            with st.spinner("Processing PDFs..."):

                new_files = process_uploads(uploaded_files)

            if new_files > 0:

                st.success(
                    f"✅ {new_files} document{'s' if new_files > 1 else ''} processed successfully."
                )

                st.rerun()

        st.divider()

        # ==========================================
        # DOCUMENTS
        # ==========================================

        st.subheader("📄 Uploaded Documents")

        if st.session_state.documents:

            for doc in st.session_state.documents:

                st.write(f"📑 **{doc['name']}**")
                st.caption(f"{doc['chunks']} Chunks")
                st.divider()

        else:

            st.info("No documents uploaded.")

        # ==========================================
        # STATS
        # ==========================================

        st.subheader("📊 Workspace")

        stats = get_stats()

        col1, col2 = st.columns(2)

        col1.metric(
            "📁 Files",
            stats["total_files"]
        )

        col2.metric(
            "📄 Chunks",
            stats["total_chunks"]
        )

        col1.metric(
            "🧠 Embeddings",
            stats["total_embeddings"]
        )

        col2.metric(
            "💾 Vector DB",
            stats["chroma_count"]
        )

        st.divider()

        # ==========================================
        # QUICK ACTIONS
        # ==========================================

        st.subheader("⚡ Quick Actions")

        if st.button(
            "🗑 Clear Database",
            use_container_width=True
        ):

            clear_database()

            st.success("Database Cleared Successfully")

            st.rerun()

        if st.button(
            "💬 Clear Chat",
            use_container_width=True
        ):

            clear_messages()

            st.success("Chat Cleared Successfully")

            st.rerun()

        st.divider()

        # ==========================================
        # FOOTER
        # ==========================================

        st.caption("ScholarAI v1.0")
        st.caption("Built with ❤️ using Streamlit & Gemini")

def handle_user_question(question: str):

    # -------------------------------
    # Validate Question
    # -------------------------------

    question = question.strip()

    if question == "":

        st.toast("⚠ Please enter a question.")

        return

    # -------------------------------
    # Check Documents
    # -------------------------------

    if not has_documents():

        st.warning(
            "📂 Please upload at least one PDF before asking questions."
        )

        return

    # -------------------------------
    # Save User Message
    # -------------------------------

    chat_history = build_chat_history()

    add_message(
        role="user",
        content=question
    )

    # -------------------------------
    # Retrieve Relevant Chunks
    # -------------------------------

    with st.spinner("🔍 Searching your documents..."):

        relevant_chunks = retrieve_relevant_chunks(question)

    if not relevant_chunks:

        st.error(
            "❌ I couldn't find any relevant information in the uploaded documents."
        )

        return

    context = "\n\n".join(relevant_chunks)

    # -------------------------------
    # Generate AI Response
    # -------------------------------

    try:

        with st.spinner("🤖 ScholarAI is thinking..."):

            answer = generate_answer(
                question=question,
                context=context,
                chat_history=chat_history,
            )

    except Exception as e:

        st.error(
            f"⚠ Something went wrong.\n\n{e}"
        )

        return

    # -------------------------------
    # Save Assistant Response
    # -------------------------------

    add_message(
        role="assistant",
        content=answer,
        sources=relevant_chunks,
    )

    st.rerun()
def generate_study_tool(tool_name):

    # =========================
    # CHECK DOCUMENTS
    # =========================

    if not has_documents():

        st.warning("📂 Please upload a PDF first.")

        return

    # =========================
    # RETRIEVE CONTEXT
    # =========================

    with st.spinner("📚 Reading your documents..."):

        relevant_chunks = retrieve_relevant_chunks(
            "Explain the complete uploaded document."
        )

    if not relevant_chunks:

        st.error("❌ No information found in the uploaded documents.")

        return

    context = "\n\n".join(relevant_chunks)

    # =========================
    # GENERATE OUTPUT
    # =========================

    with st.spinner(f"✨ Generating {tool_name.title()}..."):

        if tool_name == "summary":

            result = get_summary(context)

        elif tool_name == "notes":

            result = get_study_notes(context)

        elif tool_name == "keypoints":

            result = get_key_points(context)

        elif tool_name == "flashcards":

            flashcards = get_flashcards(context)

            st.session_state.flashcards = flashcards
            st.session_state.current_flashcard = 0
            st.session_state.show_answer = False

            st.success("📇 Flashcards Generated Successfully!")

            return

        else:

            st.error("Invalid Tool Selected.")

            return

    # =========================
    # DISPLAY OUTPUT
    # =========================

    st.success(f"✅ {tool_name.title()} Generated Successfully!")

    st.divider()

    st.subheader(f"📄 {tool_name.title()}")

    st.write(result)

    st.divider()

    # =========================
    # DOWNLOAD BUTTON
    # =========================

    st.download_button(
        label="⬇ Download as TXT",
        data=result,
        file_name=f"{tool_name}.txt",
        mime="text/plain",
        use_container_width=True,
    )

def render_chat_page():

    # =========================
    # PAGE HEADER
    # =========================

    st.title("📚 ScholarAI")
    st.caption("Research • Learn • Master")
    st.write("Your AI Research Companion")

    st.divider()

    # =========================
    # TABS
    # =========================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
        [
            "💬 Chat",
            "📄 Summary",
            "📝 Study Notes",
            "🎯 Key Points",
            "❓ Quiz",
            "📇 Flashcards",
            "🧠 Mind Map",
            "📅 Study Planner"

        ]
    )

    # =========================
    # CHAT
    # =========================

    with tab1:

        st.subheader("💬 Chat with ScholarAI")

        if not has_documents():

            st.info("Please upload PDF documents first.")

        else:

            render_chat_history()

            question = st.chat_input(
                "Ask anything about your uploaded documents..."
            )

            if question:

                handle_user_question(question)

    # =========================
    # SUMMARY
    # =========================

    with tab2:

        st.subheader("📄 AI Summary")

        if st.button(
            "Generate Summary",
            key="summary",
            use_container_width=True,
        ):
            generate_study_tool("summary")

    # =========================
    # STUDY NOTES
    # =========================

    with tab3:

        st.subheader("📝 Study Notes")

        if st.button(
            "Generate Notes",
            key="notes",
            use_container_width=True,
        ):
            generate_study_tool("notes")

    # =========================
    # KEY POINTS
    # =========================

    with tab4:

        st.subheader("🎯 Key Points")

        if st.button(
            "Generate Key Points",
            key="points",
            use_container_width=True,
        ):
            generate_study_tool("keypoints")

    # =========================
    # QUIZ
    # =========================

    with tab5:

        st.subheader("❓ AI Quiz Generator")

        if not has_documents():

            st.info("Upload a PDF first.")

        else:

            if "quiz" not in st.session_state:
                st.session_state.quiz = None

            if "submitted" not in st.session_state:
                st.session_state.submitted = False

            if st.button(
                "Generate Quiz",
                use_container_width=True,
            ):

                chunks = retrieve_relevant_chunks(
                    "Explain the complete uploaded document."
                )

                context = "\n\n".join(chunks)

                st.session_state.quiz = get_quiz(context)
                st.session_state.submitted = False

            if st.session_state.quiz:

                quiz = st.session_state.quiz

                user_answers = []

                for i, q in enumerate(quiz):

                    st.markdown(f"### Q{i+1}. {q['question']}")

                    choice = st.radio(
                        "Choose one option",
                        q["options"],
                        key=f"quiz_{i}",
                    )

                    user_answers.append(choice)

                if st.button(
                    "Submit Quiz",
                    use_container_width=True,
                ):

                    st.session_state.submitted = True

                    score = 0

                    for i, q in enumerate(quiz):

                        if user_answers[i] == q["options"][q["answer"]]:
                            score += 1

                    percentage = (score / len(quiz)) * 100

                    st.success(f"🎉 Score: {score}/{len(quiz)}")
                    st.info(f"📊 Percentage: {percentage:.2f}%")

                    st.divider()

                    st.subheader("✅ Correct Answers")

                    for i, q in enumerate(quiz):

                        st.markdown(f"**Q{i+1}.** {q['question']}")

                        st.success(
                            f"Correct Answer: {q['options'][q['answer']]}"
                        )

    # =========================
    # FLASHCARDS
    # =========================

    with tab6:

        st.subheader("📇 AI Flashcards")

        if not has_documents():

            st.info("Upload a PDF first.")

        else:

            if st.button(
                "Generate Flashcards",
                key="generate_flashcards_btn",
                use_container_width=True,
            ):

                generate_study_tool("flashcards")
                st.rerun()

            if len(st.session_state.flashcards) > 0:

                flashcards = st.session_state.flashcards

                index = st.session_state.current_flashcard

                card = flashcards[index]

                st.markdown(
                    f"### Flashcard {index+1}/{len(flashcards)}"
                )

                st.info(
                    f"❓ {card['question']}"
                )

                if st.button(
                    "Show Answer",
                    key="show_answer_btn",
                ):
                    st.session_state.show_answer = True

                if st.session_state.show_answer:

                    st.success(card["answer"])

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(
                        "⬅ Previous",
                        key="prev_flashcard",
                        disabled=index == 0,
                    ):

                        st.session_state.current_flashcard -= 1
                        st.session_state.show_answer = False
                        st.rerun()

                with col2:

                    if st.button(
                        "Next ➡",
                        key="next_flashcard",
                        disabled=index == len(flashcards) - 1,
                    ):

                        st.session_state.current_flashcard += 1
                        st.session_state.show_answer = False
                        st.rerun()
    

    

# =========================
# MIND MAP
# =========================

    with tab7:

      st.subheader("🧠 AI Mind Map")

    if st.button(
        "Generate Mind Map",
        key="mindmap_btn",
        use_container_width=True,
    ):

        chunks = retrieve_relevant_chunks(
            "Explain the complete uploaded document."
        )

        context = "\n\n".join(chunks)

        st.session_state.mindmap = get_mindmap(context)

    if st.session_state.mindmap != "":

        st.code(
            st.session_state.mindmap,
            language="text"
        )

        st.download_button(
            "Download Mind Map",
            st.session_state.mindmap,
            "mindmap.txt",
            key="download_mindmap",
        )


# =========================
# STUDY PLANNER
# =========================

    with tab8:

       st.subheader("📅 AI Study Planner")

    days = st.slider(
        "Study Duration (Days)",
        1,
        30,
        7,
        key="days_slider",
    )

    hours = st.slider(
        "Hours Per Day",
        1,
        12,
        3,
        key="hours_slider",
    )

    if st.button(
        "Generate Study Planner",
        key="study_plan_btn",
        use_container_width=True,
    ):

        chunks = retrieve_relevant_chunks(
            "Explain the complete uploaded document."
        )

        context = "\n\n".join(chunks)

        st.session_state.study_plan = get_study_plan(
            context,
            days,
            hours,
        )

    if st.session_state.study_plan != "":

        st.write(st.session_state.study_plan)

        st.download_button(
            "Download Planner",
            st.session_state.study_plan,
            "study_plan.txt",
            key="download_plan",
        )

def main():

    configure_page()
   
    init_messages()

    init_document_state()

    # Initialize Flashcards Session State
    if "flashcards" not in st.session_state:
        st.session_state.flashcards = []

    if "current_flashcard" not in st.session_state:
        st.session_state.current_flashcard = 0

    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False

    if "voice_text" not in st.session_state:
        st.session_state.voice_text = ""

    if "mindmap" not in st.session_state:
        st.session_state.mindmap = ""

    if "study_plan" not in st.session_state:
        st.session_state.study_plan = ""

    render_sidebar()

    render_chat_page()


if __name__ == "__main__":
    main()