from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.session import get_db
from app.ai.rag import rag_service

router = APIRouter()


@router.post("/query")
async def chat_query(db: AsyncSession = Depends(get_db)):
    """Send a query to the AI assistant using RAG"""
    # TODO: Implement chat query with RAG
    return {"message": "Chat query endpoint - to be implemented"}


@router.get("/sessions")
async def list_chat_sessions(db: AsyncSession = Depends(get_db)):
    """List all chat sessions for the current user"""
    # TODO: Implement list chat sessions
    return {"message": "List chat sessions endpoint - to be implemented"}


@router.get("/sessions/{session_id}")
async def get_chat_session(session_id: int, db: AsyncSession = Depends(get_db)):
    """Get a specific chat session with message history"""
    # TODO: Implement get chat session
    return {"message": f"Get chat session {session_id} endpoint - to be implemented"}


@router.websocket("/ws")
async def websocket_chat(websocket: WebSocket):
    """WebSocket endpoint for real-time chat"""
    await websocket.accept()
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()

            # TODO: Process with RAG and stream response
            response = f"Echo: {data} (WebSocket RAG to be implemented)"

            # Send response
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("Client disconnected")
