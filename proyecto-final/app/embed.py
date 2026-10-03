from google import genai
from google.genai import types

from app.config import EMBEDDING_MODEL, google_api_key


class GoogleEmbedder:
    def __init__(self) -> None:
        key = google_api_key()
        if not key:
            raise RuntimeError("Falta GOOGLE_API_KEY en el archivo .env.")
        self.client = genai.Client(api_key=key)

    def embed_documents(self, texts: list[str], titles: list[str]) -> list[list[float]]:
        prepared = [
            f"title: {title} | text: {text}"
            for text, title in zip(texts, titles)
        ]
        return self._embed_in_batches(prepared)

    def embed_query(self, question: str) -> list[float]:
        prepared = f"task: question answering | query: {question}"
        response = self.client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=prepared,
        )
        return list(response.embeddings[0].values)

    def _embed_in_batches(self, texts: list[str], batch_size: int = 20) -> list[list[float]]:
        vectors = []
        for start in range(0, len(texts), batch_size):
            contents = [
                types.Content(parts=[types.Part.from_text(text=text)])
                for text in texts[start : start + batch_size]
            ]
            response = self.client.models.embed_content(
                model=EMBEDDING_MODEL,
                contents=contents,
            )
            vectors.extend(list(item.values) for item in response.embeddings)
        return vectors

