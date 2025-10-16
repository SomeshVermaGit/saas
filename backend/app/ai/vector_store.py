from typing import List, Dict, Any
from abc import ABC, abstractmethod
from app.core.config import settings


class VectorStore(ABC):
    """Abstract base class for vector store implementations"""

    @abstractmethod
    async def add_documents(self, documents: List[Dict[str, Any]]) -> List[str]:
        """Add documents to the vector store"""
        pass

    @abstractmethod
    async def similarity_search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """Search for similar documents"""
        pass

    @abstractmethod
    async def delete_documents(self, ids: List[str]) -> bool:
        """Delete documents from the vector store"""
        pass


class MongoDBVectorStore(VectorStore):
    """MongoDB Atlas Vector Search implementation"""

    def __init__(self):
        from motor.motor_asyncio import AsyncIOMotorClient
        from pymongo import MongoClient

        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.MONGODB_DB_NAME]
        self.collection = self.db["embeddings"]

    async def add_documents(self, documents: List[Dict[str, Any]]) -> List[str]:
        """
        Add documents with embeddings to MongoDB
        Each document should have: {text, metadata, embedding}
        """
        result = await self.collection.insert_many(documents)
        return [str(id) for id in result.inserted_ids]

    async def similarity_search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """
        Perform vector similarity search using MongoDB Atlas Vector Search
        Requires Atlas Search index configured on the collection
        """
        from openai import OpenAI

        # Generate embedding for query
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        response = client.embeddings.create(
            input=query, model=settings.EMBEDDING_MODEL
        )
        query_embedding = response.data[0].embedding

        # Vector search pipeline
        pipeline = [
            {
                "$vectorSearch": {
                    "index": "vector_index",
                    "path": "embedding",
                    "queryVector": query_embedding,
                    "numCandidates": k * 10,
                    "limit": k,
                }
            },
            {
                "$project": {
                    "text": 1,
                    "metadata": 1,
                    "score": {"$meta": "vectorSearchScore"},
                }
            },
        ]

        results = []
        async for doc in self.collection.aggregate(pipeline):
            results.append(doc)

        return results

    async def delete_documents(self, ids: List[str]) -> bool:
        """Delete documents by IDs"""
        from bson import ObjectId

        object_ids = [ObjectId(id) for id in ids]
        result = await self.collection.delete_many({"_id": {"$in": object_ids}})
        return result.deleted_count > 0


class QdrantVectorStore(VectorStore):
    """Qdrant vector store implementation"""

    def __init__(self):
        from qdrant_client import AsyncQdrantClient
        from qdrant_client.models import Distance, VectorParams

        self.client = AsyncQdrantClient(
            url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY
        )
        self.collection_name = settings.QDRANT_COLLECTION_NAME

    async def add_documents(self, documents: List[Dict[str, Any]]) -> List[str]:
        """Add documents to Qdrant"""
        from qdrant_client.models import PointStruct
        import uuid

        points = []
        ids = []
        for doc in documents:
            point_id = str(uuid.uuid4())
            ids.append(point_id)
            points.append(
                PointStruct(
                    id=point_id,
                    vector=doc["embedding"],
                    payload={"text": doc["text"], "metadata": doc.get("metadata", {})},
                )
            )

        await self.client.upsert(collection_name=self.collection_name, points=points)
        return ids

    async def similarity_search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """Search for similar documents in Qdrant"""
        from openai import OpenAI

        # Generate embedding for query
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        response = client.embeddings.create(
            input=query, model=settings.EMBEDDING_MODEL
        )
        query_embedding = response.data[0].embedding

        # Search
        results = await self.client.search(
            collection_name=self.collection_name, query_vector=query_embedding, limit=k
        )

        return [
            {
                "id": str(result.id),
                "text": result.payload.get("text"),
                "metadata": result.payload.get("metadata", {}),
                "score": result.score,
            }
            for result in results
        ]

    async def delete_documents(self, ids: List[str]) -> bool:
        """Delete documents from Qdrant"""
        await self.client.delete(collection_name=self.collection_name, points_selector=ids)
        return True


def get_vector_store() -> VectorStore:
    """Factory function to get the configured vector store"""
    if settings.VECTOR_DB_TYPE == "mongodb":
        return MongoDBVectorStore()
    elif settings.VECTOR_DB_TYPE == "qdrant":
        return QdrantVectorStore()
    else:
        raise ValueError(f"Unknown vector DB type: {settings.VECTOR_DB_TYPE}")
