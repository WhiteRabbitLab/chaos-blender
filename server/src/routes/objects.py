"""
API routes for game objects
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import GameObject
from schemas import GameObjectResponse

router = APIRouter()


@router.get("/available/{blend_count}", response_model=List[GameObjectResponse])
async def get_available_objects(blend_count: int, db: Session = Depends(get_db)):
    """
    Get objects available based on current blend count
    Returns objects where unlock_threshold <= blend_count
    """
    objects = db.query(GameObject).filter(
        GameObject.unlock_threshold <= blend_count
    ).all()

    if not objects:
        raise HTTPException(status_code=404, detail="No objects available")

    return objects


@router.get("/random/{blend_count}/{count}", response_model=List[GameObjectResponse])
async def get_random_objects(
    blend_count: int,
    count: int = 3,
    db: Session = Depends(get_db)
):
    """
    Get random objects available for selection
    Returns 'count' random objects from available pool
    """
    from sqlalchemy.sql.expression import func

    objects = db.query(GameObject).filter(
        GameObject.unlock_threshold <= blend_count
    ).order_by(func.random()).limit(count).all()

    if not objects:
        raise HTTPException(status_code=404, detail="No objects available")

    return objects


@router.get("/{object_id}", response_model=GameObjectResponse)
async def get_object(object_id: int, db: Session = Depends(get_db)):
    """Get a specific game object by ID"""
    obj = db.query(GameObject).filter(GameObject.id == object_id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Object not found")

    return obj


@router.get("/", response_model=List[GameObjectResponse])
async def get_all_objects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all game objects (for admin/testing)"""
    objects = db.query(GameObject).offset(skip).limit(limit).all()
    return objects
