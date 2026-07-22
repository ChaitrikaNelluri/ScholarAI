
import google.generativeai as genai

from config import LLM_MODEL

print("Loading gemini_llm...")

from modules.study_tools import (
    generate_summary,
    generate_study_notes,
    generate_key_points,
    generate_quiz,
    generate_flashcards,
    generate_mindmap,
    generate_study_plan,
)

# Configure Gemini
genai.configure(api_key="GOOGLE_API_KEY")  
# Gemini Model
model = genai.GenerativeModel(LLM_MODEL)


def generate_answer(question, context, chat_history=""):

    prompt = f"""
You are ScholarAI.

Conversation History:
{chat_history}

Answer ONLY using the document context.

Document Context:
{context}

Question:
{question}

Rules:
1. Do not hallucinate.
2. If unavailable, reply:
"I could not find this information in the uploaded document."
3. Use headings and bullet points.
4. Keep the answer clean.

Answer:
"""

    response = model.generate_content(prompt)

    return response.text


# --------------------------
# Existing Tools
# --------------------------

def get_summary(context):
    return generate_summary(model, context)


def get_study_notes(context):
    return generate_study_notes(model, context)


def get_key_points(context):
    return generate_key_points(model, context)


def get_quiz(context):
    return generate_quiz(model, context)


def get_flashcards(context):
    return generate_flashcards(model, context)


# ======================================================
# NEW FEATURES
# ======================================================

def get_mindmap(context):

    return generate_mindmap(
        model,
        context
    )


def get_study_plan(context, days, hours):

    return generate_study_plan(
        model,
        context,
        days,
        hours
    )