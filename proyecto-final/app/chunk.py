from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader


@dataclass
class Chunk:
    source: str
    position: int
    text: str


def extract_text(filename: str, content: bytes) -> str:
    extension = Path(filename).suffix.lower()

    if extension in {".txt", ".md"}:
        return content.decode("utf-8", errors="ignore")

    if extension == ".pdf":
        reader = PdfReader(BytesIO(content))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    raise ValueError("Solo se aceptan archivos PDF, TXT o Markdown.")


def split_text(text: str, source: str, size: int = 300, overlap: int = 60) -> list[Chunk]:
    words = text.split()
    if not words:
        return []

    chunks = []
    step = size - overlap
    position = 0

    for start in range(0, len(words), step):
        part = words[start : start + size]
        if not part:
            break
        chunks.append(Chunk(source=source, position=position, text=" ".join(part)))
        position += 1
        if start + size >= len(words):
            break

    return chunks

