import os
from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are MedBot, a healthcare assistant. Provide empathetic, safe, "
    "and simple advice on common health issues (like fever, headache, anxiety, diet, exercise). "
    "Always reply in clear **Markdown format** with headings, numbered lists, and bullet points where useful. "
    "Always include a disclaimer that you're not a doctor and recommend seeing a licensed healthcare professional for serious or persistent symptoms."
)


def chatbot_response(user_msg: str) -> str:
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",  # use "gpt-4" if available
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg}
            ],
            max_tokens=300,
            temperature=0.2
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error contacting OpenAI: {e}]"
