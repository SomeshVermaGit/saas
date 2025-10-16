from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router = APIRouter()


@router.get("/me")
async def get_current_user(db: AsyncSession = Depends(get_db)):
    """Get current authenticated user"""
    # TODO: Implement get current user
    return {"message": "Get current user endpoint - to be implemented"}


@router.get("/")
async def list_users(db: AsyncSession = Depends(get_db)):
    """List all users (admin only)"""
    # TODO: Implement list users
    return {"message": "List users endpoint - to be implemented"}


@router.put("/{user_id}")
async def update_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Update user details"""
    # TODO: Implement update user
    return {"message": "Update user endpoint - to be implemented"}
