import React from 'react';
import './GameHeader.css';

interface GameHeaderProps {
  blendCount: number;
  onShowLeaderboard: () => void;
  onReset: () => void;
}

function GameHeader({ blendCount, onShowLeaderboard, onReset }: GameHeaderProps) {
  return (
    <header className="game-header">
      <div className="header-content">
        <div className="header-stats">
          <div className="stat">
            <span className="stat-label">BLENDS:</span>
            <span className="stat-value">{blendCount}</span>
          </div>
        </div>
        <h1 className="game-title glow">NORMAL BLENDER</h1>
        <div className="header-buttons">
          <button className="header-btn" onClick={onShowLeaderboard}>
            LEADERBOARD
          </button>
          <button className="header-btn reset-btn" onClick={onReset}>
            RESET
          </button>
        </div>
      </div>
    </header>
  );
}

export default GameHeader;
