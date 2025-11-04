"""
API routes for leaderboards
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List, Optional

from database import get_db
from models import Leaderboard, PlayerScore, ScoringSystem
from schemas import LeaderboardEntry, LeaderboardResponse

router = APIRouter()


@router.get("/{scoring_system}", response_model=LeaderboardResponse)
async def get_leaderboard(
    scoring_system: str,
    limit: int = Query(default=100, le=500),
    db: Session = Depends(get_db)
):
    """
    Get leaderboard for a specific scoring system
    Returns top scores for the given scoring system
    """
    # Query leaderboard entries
    entries = db.query(Leaderboard).filter(
        Leaderboard.scoring_system == scoring_system
    ).order_by(desc(Leaderboard.score)).limit(limit).all()

    # Add rank to each entry
    leaderboard_entries = []
    for rank, entry in enumerate(entries, start=1):
        leaderboard_entries.append(
            LeaderboardEntry(
                player_name=entry.player_name,
                scoring_system=entry.scoring_system,
                score=entry.score,
                blend_count=entry.blend_count,
                achieved_at=entry.achieved_at,
                rank=rank
            )
        )

    total = db.query(Leaderboard).filter(
        Leaderboard.scoring_system == scoring_system
    ).count()

    return LeaderboardResponse(
        scoring_system=scoring_system,
        entries=leaderboard_entries,
        total_entries=total
    )


@router.get("/", response_model=List[str])
async def get_available_leaderboards(db: Session = Depends(get_db)):
    """Get list of all scoring systems with leaderboard entries"""
    systems = db.query(Leaderboard.scoring_system).distinct().all()
    return [system[0] for system in systems]


@router.post("/submit/{session_id}")
async def submit_to_leaderboard(
    session_id: str,
    player_name: str = Query(..., min_length=1, max_length=50),
    db: Session = Depends(get_db)
):
    """
    Submit current session scores to the global leaderboard
    """
    # Get player session
    player_score = db.query(PlayerScore).filter(
        PlayerScore.session_id == session_id
    ).first()

    if not player_score:
        raise HTTPException(status_code=404, detail="Session not found")

    if not player_score.scores:
        raise HTTPException(status_code=400, detail="No scores to submit")

    # Update player name
    player_score.player_name = player_name

    # Create leaderboard entries for each scoring system
    submitted_systems = []
    for scoring_system, score in player_score.scores.items():
        # Check if entry already exists for this session
        existing = db.query(Leaderboard).filter(
            Leaderboard.session_id == session_id,
            Leaderboard.scoring_system == scoring_system
        ).first()

        if not existing:
            leaderboard_entry = Leaderboard(
                player_name=player_name,
                scoring_system=scoring_system,
                score=score,
                blend_count=player_score.blend_count,
                session_id=session_id
            )
            db.add(leaderboard_entry)
            submitted_systems.append(scoring_system)

    db.commit()

    return {
        "message": "Scores submitted successfully",
        "player_name": player_name,
        "systems_submitted": submitted_systems,
        "total_systems": len(submitted_systems)
    }


@router.get("/player/{player_name}", response_model=List[LeaderboardEntry])
async def get_player_scores(
    player_name: str,
    db: Session = Depends(get_db)
):
    """Get all leaderboard entries for a specific player"""
    entries = db.query(Leaderboard).filter(
        Leaderboard.player_name == player_name
    ).order_by(desc(Leaderboard.achieved_at)).all()

    if not entries:
        raise HTTPException(status_code=404, detail="Player not found on leaderboard")

    return [
        LeaderboardEntry(
            player_name=entry.player_name,
            scoring_system=entry.scoring_system,
            score=entry.score,
            blend_count=entry.blend_count,
            achieved_at=entry.achieved_at
        )
        for entry in entries
    ]
