"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from datetime import datetime


class GameObjectBase(BaseModel):
    """Base schema for game objects"""
    name: str
    category: str
    unlock_threshold: int = 0
    sprite_path: str
    scores: Dict[str, float]
    description: Optional[str] = None
    rarity: str = "common"
    color: Optional[str] = None


class GameObjectCreate(GameObjectBase):
    """Schema for creating game objects"""
    pass


class GameObjectResponse(GameObjectBase):
    """Schema for game object responses"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ScoringSystemBase(BaseModel):
    """Base schema for scoring systems"""
    name: str
    display_name: str
    description: Optional[str] = None
    unit: str = "points"
    icon: Optional[str] = None
    visible_from_start: bool = False


class ScoringSystemCreate(ScoringSystemBase):
    """Schema for creating scoring systems"""
    pass


class ScoringSystemResponse(ScoringSystemBase):
    """Schema for scoring system responses"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class BlendRequest(BaseModel):
    """Schema for blend requests"""
    session_id: str
    object_ids: List[int]


class BlendResponse(BaseModel):
    """Schema for blend responses"""
    success: bool
    blend_count: int
    scores_added: Dict[str, float]
    total_scores: Dict[str, float]
    newly_unlocked_systems: List[str]
    newly_unlocked_objects: List[GameObjectResponse]


class PlayerScoreCreate(BaseModel):
    """Schema for creating/updating player scores"""
    player_name: str
    session_id: str
    scores: Dict[str, float]
    blend_count: int
    blended_objects: List[int]


class PlayerScoreResponse(BaseModel):
    """Schema for player score responses"""
    id: int
    player_name: str
    session_id: str
    blend_count: int
    scores: Dict[str, float]
    blended_objects: List[int]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class LeaderboardEntry(BaseModel):
    """Schema for leaderboard entries"""
    player_name: str
    scoring_system: str
    score: float
    blend_count: int
    achieved_at: datetime
    rank: Optional[int] = None

    class Config:
        from_attributes = True


class LeaderboardResponse(BaseModel):
    """Schema for leaderboard responses"""
    scoring_system: str
    entries: List[LeaderboardEntry]
    total_entries: int


class SessionResponse(BaseModel):
    """Schema for session info responses"""
    session_id: str
    blend_count: int
    scores: Dict[str, float]
    unlocked_systems: List[str]
    available_objects: List[GameObjectResponse]
