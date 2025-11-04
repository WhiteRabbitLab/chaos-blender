"""
API routes for scoring and blending
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, List
import uuid

from database import get_db
from models import GameObject, ScoringSystem, PlayerScore
from schemas import (
    BlendRequest,
    BlendResponse,
    SessionResponse,
    GameObjectResponse,
    PlayerScoreCreate,
    PlayerScoreResponse
)

router = APIRouter()


@router.post("/blend", response_model=BlendResponse)
async def blend_objects(request: BlendRequest, db: Session = Depends(get_db)):
    """
    Process a blend request - add object(s) to the blend and calculate scores
    """
    # Get or create player score session
    player_score = db.query(PlayerScore).filter(
        PlayerScore.session_id == request.session_id
    ).first()

    if not player_score:
        # Create new session
        player_score = PlayerScore(
            player_name="Anonymous",
            session_id=request.session_id,
            blend_count=0,
            scores={},
            blended_objects=[]
        )
        db.add(player_score)

    # Get the objects being blended
    objects = db.query(GameObject).filter(GameObject.id.in_(request.object_ids)).all()

    if len(objects) != len(request.object_ids):
        raise HTTPException(status_code=404, detail="One or more objects not found")

    # Check if objects are unlocked
    for obj in objects:
        if obj.unlock_threshold > player_score.blend_count:
            raise HTTPException(
                status_code=403,
                detail=f"Object '{obj.name}' is not yet unlocked"
            )

    # Calculate score additions
    scores_added: Dict[str, float] = {}
    for obj in objects:
        for scoring_system, value in obj.scores.items():
            scores_added[scoring_system] = scores_added.get(scoring_system, 0) + value

    # Update player scores (preserves all existing systems)
    current_scores = player_score.scores or {}
    for scoring_system, value in scores_added.items():
        current_scores[scoring_system] = current_scores.get(scoring_system, 0) + value

    # Track newly unlocked scoring systems
    newly_unlocked_systems = []
    existing_systems = set(player_score.scores.keys()) if player_score.scores else set()
    for system in scores_added.keys():
        if system not in existing_systems:
            newly_unlocked_systems.append(system)

    # Update blend count and blended objects
    player_score.blend_count += len(objects)
    blended_list = player_score.blended_objects or []
    blended_list.extend(request.object_ids)
    player_score.blended_objects = blended_list
    player_score.scores = current_scores

    # Check for newly unlocked objects
    previous_count = player_score.blend_count - len(objects)
    newly_unlocked_objects = db.query(GameObject).filter(
        GameObject.unlock_threshold > previous_count,
        GameObject.unlock_threshold <= player_score.blend_count
    ).all()

    db.commit()
    db.refresh(player_score)

    return BlendResponse(
        success=True,
        blend_count=player_score.blend_count,
        scores_added=scores_added,
        total_scores=current_scores,
        newly_unlocked_systems=newly_unlocked_systems,
        newly_unlocked_objects=[
            GameObjectResponse.model_validate(obj) for obj in newly_unlocked_objects
        ]
    )


@router.get("/session/{session_id}", response_model=SessionResponse)
async def get_session(session_id: str, db: Session = Depends(get_db)):
    """Get current session information"""
    player_score = db.query(PlayerScore).filter(
        PlayerScore.session_id == session_id
    ).first()

    if not player_score:
        # Return new session
        return SessionResponse(
            session_id=session_id,
            blend_count=0,
            scores={},
            unlocked_systems=[],
            available_objects=[]
        )

    # Get available objects
    available_objects = db.query(GameObject).filter(
        GameObject.unlock_threshold <= player_score.blend_count
    ).all()

    return SessionResponse(
        session_id=session_id,
        blend_count=player_score.blend_count,
        scores=player_score.scores or {},
        unlocked_systems=list((player_score.scores or {}).keys()),
        available_objects=[
            GameObjectResponse.model_validate(obj) for obj in available_objects
        ]
    )


@router.post("/reset/{session_id}")
async def reset_session(session_id: str, db: Session = Depends(get_db)):
    """Reset a player session"""
    player_score = db.query(PlayerScore).filter(
        PlayerScore.session_id == session_id
    ).first()

    if player_score:
        db.delete(player_score)
        db.commit()

    return {"message": "Session reset successfully", "session_id": session_id}


@router.get("/new-session")
async def create_new_session():
    """Generate a new session ID"""
    return {"session_id": str(uuid.uuid4())}
