from typing import List, Dict, Any
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from app.core.config import settings
from app.ai.vector_store import get_vector_store


class RAGService:
    """Service for Retrieval Augmented Generation"""

    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.OPENAI_MODEL,
            api_key=settings.OPENAI_API_KEY,
            temperature=0.7,
        )
        self.embeddings = OpenAIEmbeddings(
            model=settings.EMBEDDING_MODEL, api_key=settings.OPENAI_API_KEY
        )
        self.vector_store = get_vector_store()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, length_function=len
        )

    async def process_document(
        self, text: str, metadata: Dict[str, Any]
    ) -> List[str]:
        """
        Process a document: split into chunks, create embeddings, store in vector DB
        """
        # Split text into chunks
        chunks = self.text_splitter.split_text(text)

        # Create embeddings for each chunk
        documents = []
        for i, chunk in enumerate(chunks):
            embedding = await self.embeddings.aembed_query(chunk)
            documents.append(
                {
                    "text": chunk,
                    "embedding": embedding,
                    "metadata": {**metadata, "chunk_index": i, "total_chunks": len(chunks)},
                }
            )

        # Store in vector database
        ids = await self.vector_store.add_documents(documents)
        return ids

    async def query(
        self, question: str, k: int = 5, conversation_history: List[Dict] = None
    ) -> Dict[str, Any]:
        """
        Answer a question using RAG
        """
        # Retrieve relevant documents
        relevant_docs = await self.vector_store.similarity_search(question, k=k)

        # Build context from retrieved documents
        context = "\n\n".join([doc["text"] for doc in relevant_docs])

        # Create prompt
        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are an AI assistant helping employees find information from company documents.
Use the following context to answer the question. If you cannot find the answer in the context, say so.
Be concise and accurate.

Context:
{context}""",
                ),
                ("human", "{question}"),
            ]
        )

        # Generate answer
        messages = prompt_template.format_messages(context=context, question=question)
        response = await self.llm.ainvoke(messages)

        return {
            "answer": response.content,
            "sources": [
                {
                    "text": doc["text"][:200] + "...",
                    "metadata": doc.get("metadata", {}),
                    "score": doc.get("score", 0),
                }
                for doc in relevant_docs
            ],
        }

    async def summarize_document(self, text: str, max_length: int = 500) -> str:
        """Generate a summary of a document"""
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"Summarize the following document in approximately {max_length} words. Be concise and capture the key points.",
                ),
                ("human", "{text}"),
            ]
        )

        messages = prompt.format_messages(text=text)
        response = await self.llm.ainvoke(messages)
        return response.content

    async def delete_document_embeddings(self, vector_ids: List[str]) -> bool:
        """Delete document embeddings from vector store"""
        return await self.vector_store.delete_documents(vector_ids)


# Singleton instance
rag_service = RAGService()
