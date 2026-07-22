from modules.gemini_llm import generate_answer


def generate_mindmap(context):

    prompt = f"""
You are an expert teacher.

Generate a clean hierarchical text mind map from the following study material.

Rules:
- Start with the main topic.
- Use branches.
- Use indentation.
- Keep it easy to understand.
- Don't explain anything outside the mind map.

Study Material:
{context}
"""

    return generate_answer(prompt)