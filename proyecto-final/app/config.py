import os
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

CHROMA_PATH = ROOT / "chroma"
COLLECTION_NAME = "apuntes_ia"
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "gemini-embedding-2")
GENERATION_MODEL = os.getenv("GENERATION_MODEL", "gemini-3.5-flash-lite")
MIN_SCORE = float(os.getenv("MIN_SCORE", "0.35"))


def google_api_key() -> str:
    return os.getenv("GOOGLE_API_KEY", "").strip()

