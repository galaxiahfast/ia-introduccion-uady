from google import genai

from app.config import GENERATION_MODEL, MIN_SCORE, google_api_key


ABSTENTION = "No tengo evidencia suficiente en los documentos para responder esa pregunta."


class GoogleGenerator:
    def __init__(self) -> None:
        key = google_api_key()
        if not key:
            raise RuntimeError("Falta GOOGLE_API_KEY en el archivo .env.")
        self.client = genai.Client(api_key=key)

    def answer(self, question: str, citations: list[dict]) -> tuple[str, bool]:
        if not citations or citations[0]["score"] < MIN_SCORE:
            return ABSTENTION, True

        context = "\n\n".join(
            f"[{number}] Fuente: {item['source']}\n{item['text']}"
            for number, item in enumerate(citations, start=1)
        )
        prompt = f"""Eres un asistente para consultar apuntes de Inteligencia Artificial.
Responde en español y solamente con la evidencia incluida abajo.
Usa citas como [1] o [2] después de cada afirmación.
Si la evidencia no responde la pregunta, escribe exactamente: NO_HAY_EVIDENCIA
Sé breve y no agregues información externa.

EVIDENCIA
{context}

PREGUNTA
{question}
"""
        response = self.client.models.generate_content(
            model=GENERATION_MODEL,
            contents=prompt,
        )
        answer = (response.text or "").strip()
        if not answer or "NO_HAY_EVIDENCIA" in answer:
            return ABSTENTION, True
        return answer, False

