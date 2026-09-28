from typing import Annotated

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.chunk import extract_text, split_text
from app.config import EMBEDDING_MODEL, GENERATION_MODEL, google_api_key
from app.embed import GoogleEmbedder
from app.generate import GoogleGenerator
from app.store import VectorStore


app = FastAPI(title="API del asistente RAG", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://127.0.0.1:8501"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str = Field(min_length=1)
    top_k: int = Field(default=3, ge=1, le=8)


@app.get("/health")
def health() -> dict:
    store = VectorStore()
    return {
        "status": "ok",
        "chunks": store.count(),
        "api_key_configured": bool(google_api_key()),
        "embedding_model": EMBEDDING_MODEL,
        "generation_model": GENERATION_MODEL,
    }


@app.post("/ingest")
async def ingest(files: Annotated[list[UploadFile], File(...)]) -> dict:
    if not google_api_key():
        raise HTTPException(status_code=503, detail="Falta GOOGLE_API_KEY en .env.")

    all_chunks = []
    accepted_documents = 0

    for file in files:
        try:
            content = await file.read()
            text = extract_text(file.filename or "documento.txt", content)
            chunks = split_text(text, file.filename or "documento.txt")
        except ValueError as error:
            raise HTTPException(status_code=400, detail=str(error)) from error

        if chunks:
            accepted_documents += 1
            all_chunks.extend(chunks)

    if not all_chunks:
        raise HTTPException(status_code=400, detail="Los archivos no contienen texto utilizable.")

    try:
        embedder = GoogleEmbedder()
        vectors = embedder.embed_documents(
            [chunk.text for chunk in all_chunks],
            [chunk.source for chunk in all_chunks],
        )
        VectorStore().add(all_chunks, vectors)
    except Exception as error:
        raise HTTPException(status_code=502, detail=f"No se pudo indexar con Google AI: {error}") from error

    return {
        "message": "Documentos indexados correctamente.",
        "documents": accepted_documents,
        "chunks": len(all_chunks),
        "total_chunks": VectorStore().count(),
    }


@app.post("/query")
def query(request: QueryRequest) -> dict:
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Escribe una pregunta.")
    if not google_api_key():
        raise HTTPException(status_code=503, detail="Falta GOOGLE_API_KEY en .env.")

    store = VectorStore()
    if store.count() == 0:
        raise HTTPException(status_code=400, detail="El corpus todavía no ha sido indexado.")

    try:
        query_vector = GoogleEmbedder().embed_query(question)
        citations = store.search(query_vector, request.top_k)
        answer, abstained = GoogleGenerator().answer(question, citations)
    except Exception as error:
        raise HTTPException(status_code=502, detail=f"No se pudo consultar Google AI: {error}") from error

    return {
        "answer": answer,
        "citations": citations,
        "abstained": abstained,
    }

