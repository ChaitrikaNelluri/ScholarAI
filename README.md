<div align="center">

# 📚 ScholarAI

### *Transforming PDFs into an Intelligent Learning Experience*

An AI-powered Research Paper & Study Assistant that enables users to chat with documents, generate summaries, create quizzes, flashcards, study notes, mind maps, and personalized study plans using Retrieval-Augmented Generation (RAG).

<p>

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-green?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Database-orange?style=for-the-badge)

</p>

</div>

---

# 🌟 Overview

Reading research papers, textbooks, and technical PDFs can be time-consuming.

**ScholarAI** acts as an intelligent study companion that understands your uploaded documents and allows you to interact with them naturally.

Instead of searching page by page, simply ask questions in plain English and receive context-aware answers powered by AI.

ScholarAI also helps learners prepare efficiently by automatically generating:

- 📄 Summaries
- 📝 Study Notes
- 🎯 Key Points
- ❓ AI Quizzes
- 📇 Flashcards
- 🧠 Mind Maps
- 📅 Personalized Study Plans

---

# ✨ Key Features

## 💬 Chat with Documents

- Upload PDF files
- Ask questions naturally
- Context-aware AI responses
- Retrieval-Augmented Generation (RAG)

---

## 📄 AI Summary

Generate concise summaries from lengthy documents within seconds.

---

## 📝 Smart Study Notes

Convert complex documents into well-structured notes for quick revision.

---

## 🎯 Key Points Extraction

Automatically identify the most important concepts and highlights.

---

## ❓ Quiz Generator

Generate multiple-choice quizzes to test your understanding.

- Instant scoring
- Correct answer evaluation
- Interactive learning

---

## 📇 Flashcards

Create AI-generated flashcards for efficient revision.

- Question
- Answer
- Easy navigation

---

## 🧠 Mind Map Generator

Visualize document concepts as structured hierarchical text.

---

## 📅 AI Study Planner

Generate personalized study schedules based on:

- Study duration
- Daily study hours

---

# 🏗 Architecture

```text
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
            ChromaDB Vector Store
                       │
                       ▼
             Semantic Retrieval
                       │
                       ▼
                Google Gemini AI
                       │
                       ▼
      ┌─────────────────────────────────┐
      │ Chat │ Summary │ Quiz │ Notes   │
      │ Flashcards │ Mind Map │ Planner │
      └─────────────────────────────────┘
```

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini |
| RAG | LangChain |
| Embeddings | Sentence Transformers |
| Vector Database | ChromaDB |
| PDF Processing | PyMuPDF |
| Environment | Python Virtual Environment |

---

# 📂 Project Structure

```text
ScholarAI
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── assets
│   └── style.css
│
└── modules
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

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/ChaitrikaNelluri/ScholarAI.git
```

---

## Navigate into the Project

```bash
cd ScholarAI
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

---

## Activate the Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create a `.env` File

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# ⚙️ How ScholarAI Works

1. Upload one or more PDF documents.
2. Extract text from PDFs.
3. Split text into meaningful chunks.
4. Generate embeddings.
5. Store embeddings inside ChromaDB.
6. Retrieve relevant content using semantic similarity.
7. Generate AI responses with Google Gemini.
8. Display answers and learning resources to the user.

---

# 📸 Screenshots

> Add screenshots after deployment.

- Home Page
- Chat Interface
- Summary
- Quiz
- Flashcards
- Mind Map
- Study Planner

---

# 🎯 Future Roadmap

- 🎤 Voice Interaction
- 📚 Multi-document Chat
- 📑 Citation Support
- 📌 PDF Highlighting
- 🧠 Conversation Memory
- 👤 User Authentication
- 🌙 Dark Mode
- 📤 Export Notes as PDF
- 📊 AI Analytics Dashboard
- 🤖 Research Paper Comparison
- 🎞 AI Presentation Generator

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are always welcome.

If you'd like to improve ScholarAI:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👩‍💻 Developer

## Chaitrika Chowdary

Computer Science & Information Technology Student

Passionate about Artificial Intelligence, Machine Learning, Data Science, and building AI-powered applications that solve real-world problems.

GitHub: https://github.com/ChaitrikaNelluri

---

<div align="center">

### ⭐ If you like ScholarAI, consider giving it a Star!

*"Making research and learning smarter with AI."*

</div>
