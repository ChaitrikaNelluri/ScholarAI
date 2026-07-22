# 📚 ScholarAI

> **An AI-Powered Research Paper & Study Assistant built with Retrieval-Augmented Generation (RAG), Streamlit, Gemini AI, and ChromaDB.**

ScholarAI helps students, researchers, and professionals interact with PDF documents using AI. Instead of reading lengthy research papers manually, users can upload PDFs and ask questions, generate summaries, create quizzes, flashcards, study notes, mind maps, and personalized study plans—all in one place.

---

## 🚀 Features

### 💬 AI Chat
- Ask questions about uploaded PDF documents
- Context-aware responses using RAG
- Natural language interaction

### 📄 AI Summary
- Generate concise summaries
- Capture the main ideas instantly

### 📝 Study Notes
- Convert lengthy documents into organized notes
- Easy to revise before exams

### 🎯 Key Points
- Extract important concepts
- Highlight essential information

### ❓ AI Quiz Generator
- Automatically generate multiple-choice quizzes
- Evaluate understanding of the uploaded document

### 📇 Flashcards
- AI-generated question-answer flashcards
- Great for quick revision

### 🧠 Mind Map Generator
- Convert document content into structured mind maps
- Understand relationships between concepts

### 📅 AI Study Planner
- Generate personalized study schedules
- Customize based on study duration and daily study hours

---

# 🏗️ System Architecture

```
               PDF Upload
                    │
                    ▼
            PDF Text Extraction
                    │
                    ▼
              Text Chunking
                    │
                    ▼
          Sentence Embeddings
                    │
                    ▼
              ChromaDB Storage
                    │
                    ▼
          Semantic Retrieval (RAG)
                    │
                    ▼
            Google Gemini AI
                    │
                    ▼
      Chat • Summary • Notes • Quiz
 Flashcards • Mind Map • Study Planner
```

---

# 🛠️ Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## AI & LLM

- Google Gemini
- Sentence Transformers

## Vector Database

- ChromaDB

## PDF Processing

- PyMuPDF

## Retrieval-Augmented Generation

- LangChain

## Machine Learning

- Hugging Face Sentence Transformers

---

# 📂 Project Structure

```
ScholarAI/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── assets/
│   └── style.css
│
└── modules/
    ├── chat_manager.py
    ├── document_manager.py
    ├── embeddings.py
    ├── gemini_llm.py
    ├── mindmap.py
    ├── pdf_reader.py
    ├── retriever.py
    ├── study_planner.py
    ├── study_tools.py
    ├── text_chunker.py
    ├── vector_store.py
    └── voice_assistant.py
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/ChaitrikaNelluri/ScholarAI.git
```

Move into the project directory

```bash
cd ScholarAI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 💡 How It Works

1. Upload one or more PDF documents.
2. ScholarAI extracts the text.
3. The text is divided into chunks.
4. Each chunk is converted into embeddings.
5. Embeddings are stored in ChromaDB.
6. Relevant chunks are retrieved using semantic search.
7. Gemini AI generates accurate, context-aware responses.

---

# 📸 Screenshots

Add screenshots here after deployment.

Example:

```
Home Page

Chat Interface

Quiz Generator

Flashcards

Mind Map

Study Planner
```

---

# 🔮 Future Improvements

- Voice interaction
- Multi-document chat
- Citation support
- PDF highlighting
- Conversation memory
- User authentication
- Dark mode
- Export notes as PDF
- Export flashcards
- Research paper comparison
- AI presentation generator

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, create a new branch, and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Chaitrika Chowdary**

- GitHub: https://github.com/ChaitrikaNelluri

---

⭐ If you found this project useful, consider giving it a star!
