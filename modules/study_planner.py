
def generate_study_plan(model, context, days, hours):

    prompt = f"""
You are an expert study planner.

Create a {days}-day study plan.

Hours available per day: {hours}

Study Material:

{context}

For every day include:
- Divide the syllabus evenly.
- Include revision sessions.
- Include short breaks.
- Mention daily learning goals.
- End with a final revision day.
- Present the plan in a clean table format.


- Topics
- Hours Allocation
- Revision
- Practice Questions
- Expected Outcome
"""

    response = model.generate_content(prompt)

    return response.text












