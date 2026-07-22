
print("Loading study_tools...")
import google.generativeai as genai
import json




def generate_summary(model, context):

    prompt = f"""
You are ScholarAI.

Generate a concise summary of the document.

Document:
{context}
"""

    response = model.generate_content(prompt)

    return response.text


def generate_study_notes(model, context):

    prompt = f"""
You are ScholarAI.

Generate detailed study notes.

Requirements:
- Headings
- Bullet Points
- Easy to Understand

Document:
{context}
"""

    response = model.generate_content(prompt)

    return response.text


def generate_key_points(model, context):

    prompt = f"""
Extract the most important key points.

Maximum 15 points.

Document:
{context}
"""

    response = model.generate_content(prompt)

    return response.text


def generate_quiz(model, context):

    prompt = f"""
You are an expert exam paper generator.

Generate EXACTLY 10 MCQs from the document.

Return ONLY valid JSON.

Format:

[
{{
"question":"...",
"options":[
"Option A",
"Option B",
"Option C",
"Option D"
],
"answer":0
}}
]

Rules:

- Exactly 10 questions.
- Four options.
- answer must be 0,1,2 or 3.
- No explanation.
- Return ONLY JSON.

Document:

{context}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    try:
        quiz = json.loads(text)
    except Exception:
        quiz = []

    return quiz

def generate_flashcards(model, context):

    prompt = f"""
You are an expert teacher.

Generate EXACTLY 15 flashcards from the document.

Return ONLY valid JSON.

Format:

[
    {{
        "question":"...",
        "answer":"..."
    }}
]

Rules:

- Exactly 15 flashcards.
- Keep questions short.
- Keep answers concise.
- Return ONLY JSON.
- No markdown.
- No explanation.

Document:

{context}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    try:
        flashcards = json.loads(text)
    except Exception:
        flashcards = []

    
    return flashcards

print(
    "generate_flashcards exists:",
    "generate_flashcards" in globals()
)

# ==========================================================
# AI MIND MAP
# ==========================================================

def generate_mindmap(model, context):

    prompt = f"""
You are an expert teacher.

Read the document and create a hierarchical mind map.

Rules:
- Use Markdown.
- Use headings and nested bullet points.
- Start from the main topic.
- Show relationships clearly.
- Do not include explanations outside the mind map.

Document:

{context}
"""

    response = model.generate_content(prompt)

    return response.text


# ==========================================================
# AI STUDY PLANNER
# ==========================================================

def generate_study_plan(model, context, days, hours):

    prompt = f"""
You are an expert study coach.

Create a {days}-day study plan.

The student can study {hours} hours per day.

Requirements:

- Divide the syllabus across all {days} days.
- Mention daily topics.
- Mention learning objectives.
- Mention revision schedule.
- Mention practice tasks.
- Ensure the workload fits within {hours} hours per day.
- Use Markdown.

Document:

{context}
"""

    response = model.generate_content(prompt)

    return response.text