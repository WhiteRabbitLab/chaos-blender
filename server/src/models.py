"""
SQLAlchemy models for Chaos Blender
"""
from sqlalchemy import Column, Integer, String, Float, Boolean, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class GameObject(Base):
    """Model for blendable game objects"""
    __tablename__ = "game_objects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    category = Column(String, nullable=False)  # fruit, vegetable, absurd, magical, etc.
    unlock_threshold = Column(Integer, default=0)  # Number of blends required to unlock
    sprite_path = Column(String, nullable=False)  # Path to pixel art sprite

    # Scoring system contributions (JSON object with scoring system names as keys)
    # Example: {"nutritional_value": 15.5, "impossibility_index": 42.7, "deep_lore": 3}
    scores = Column(JSON, nullable=False)

    # Metadata
    description = Column(String)
    rarity = Column(String, default="common")  # common, uncommon, rare, epic, legendary
    color = Column(String)  # Hex color code for the object (e.g., "#FF5733")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ScoringSystem(Base):
    """Model for scoring systems"""
    __tablename__ = "scoring_systems"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    display_name = Column(String, nullable=False)
    description = Column(String)
    unit = Column(String, default="points")  # Can be weird units like "souls", "vibes", etc.
    icon = Column(String)  # Emoji or icon identifier
    visible_from_start = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class PlayerScore(Base):
    """Model for player scores"""
    __tablename__ = "player_scores"

    id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String, nullable=False, index=True)
    session_id = Column(String, nullable=False, index=True)

    # Total blend count for this session
    blend_count = Column(Integer, default=0)

    # Scores for each scoring system (JSON object)
    # Example: {"nutritional_value": 1250.5, "impossibility_index": 3847.2}
    scores = Column(JSON, nullable=False)

    # Objects blended in this session (list of object IDs)
    blended_objects = Column(JSON, nullable=False)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Leaderboard(Base):
    """Model for leaderboard entries"""
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String, nullable=False, index=True)
    scoring_system = Column(String, nullable=False, index=True)
    score = Column(Float, nullable=False)
    blend_count = Column(Integer, nullable=False)
    session_id = Column(String, nullable=False)

    # Timestamp
    achieved_at = Column(DateTime(timezone=True), server_default=func.now())
