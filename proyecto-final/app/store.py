from dataclasses import asdict
from uuid import uuid4

import chromadb

from app.chunk import Chunk
from app.config import CHROMA_PATH, COLLECTION_NAME


class VectorStore:
    def __init__(self) -> None:
        self.client = chromadb.PersistentClient(path=str(CHROMA_PATH))
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )

    def count(self) -> int:
        return self.collection.count()

    def add(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        sources = sorted({chunk.source for chunk in chunks})
        for source in sources:
            self.collection.delete(where={"source": source})

        self.collection.add(
            ids=[str(uuid4()) for _ in chunks],
            documents=[chunk.text for chunk in chunks],
            metadatas=[asdict(chunk) | {"title": chunk.source} for chunk in chunks],
            embeddings=embeddings,
        )

    def search(self, embedding: list[float], top_k: int) -> list[dict]:
        amount = min(top_k, self.count())
        if amount == 0:
            return []

        result = self.collection.query(
            query_embeddings=[embedding],
            n_results=amount,
            include=["documents", "metadatas", "distances"],
        )

        hits = []
        for item_id, text, metadata, distance in zip(
            result["ids"][0],
            result["documents"][0],
            result["metadatas"][0],
            result["distances"][0],
        ):
            hits.append(
                {
                    "id": item_id,
                    "source": metadata["source"],
                    "position": metadata["position"],
                    "text": text,
                    "score": round(max(0.0, 1.0 - float(distance)), 4),
                }
            )
        return hits

