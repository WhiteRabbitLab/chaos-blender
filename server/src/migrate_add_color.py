"""
Migration script to add color column to GameObject table
"""
from database import SessionLocal, engine, Base
from models import GameObject, ScoringSystem, PlayerScore, Leaderboard

def migrate():
    """Drop and recreate all tables with new schema"""
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)

    print("Creating tables with new schema...")
    Base.metadata.create_all(bind=engine)

    print("✓ Migration complete! Run init_data.py to repopulate the database.")

if __name__ == "__main__":
    migrate()
