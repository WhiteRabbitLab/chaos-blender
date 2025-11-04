import React, { useState, useEffect } from 'react';
import './Leaderboard.css';
import { getLeaderboard, submitToLeaderboard, getAvailableLeaderboards } from '../utils/api';
import { LeaderboardEntry } from '../types';

interface LeaderboardProps {
  sessionId: string;
  currentScores: Record<string, number>;
  blendCount: number;
  onClose: () => void;
}

function Leaderboard({ sessionId, currentScores, blendCount, onClose }: LeaderboardProps) {
  const [selectedSystem, setSelectedSystem] = useState<string>('');
  const [availableSystems, setAvailableSystems] = useState<string[]>([]);
  const [entries, setEntries] = useState<LeaderboardEntry[]>([]);
  const [loading, setLoading] = useState(false);
  const [playerName, setPlayerName] = useState('');
  const [hasSubmitted, setHasSubmitted] = useState(false);

  // Load available leaderboards on mount
  useEffect(() => {
    loadAvailableLeaderboards();
  }, []);

  // Load leaderboard when system changes
  useEffect(() => {
    if (selectedSystem) {
      loadLeaderboard();
    }
  }, [selectedSystem]);

  const loadAvailableLeaderboards = async () => {
    try {
      const systems = await getAvailableLeaderboards();
      setAvailableSystems(systems);
      if (systems.length > 0 && !selectedSystem) {
        setSelectedSystem(systems[0]);
      }
    } catch (error) {
      console.error('Error loading leaderboards:', error);
      // If no leaderboards exist yet, use current scores
      const systems = Object.keys(currentScores);
      if (systems.length > 0) {
        setAvailableSystems(systems);
        setSelectedSystem(systems[0]);
      }
    }
  };

  const loadLeaderboard = async () => {
    if (!selectedSystem) return;

    setLoading(true);
    try {
      const data = await getLeaderboard(selectedSystem, 50);
      setEntries(data.entries);
    } catch (error) {
      console.error('Error loading leaderboard:', error);
      setEntries([]);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async () => {
    if (!playerName.trim()) {
      alert('Please enter your name!');
      return;
    }

    try {
      await submitToLeaderboard(sessionId, playerName.trim());
      setHasSubmitted(true);
      alert('Scores submitted successfully!');
      loadLeaderboard(); // Reload to show new entry
    } catch (error) {
      console.error('Error submitting scores:', error);
      alert('Failed to submit scores. Please try again.');
    }
  };

  const formatSystemName = (system: string): string => {
    return system.replace(/_/g, ' ').toUpperCase();
  };

  const formatDate = (dateString: string): string => {
    const date = new Date(dateString);
    return date.toLocaleDateString();
  };

  return (
    <div className="leaderboard-overlay" onClick={onClose}>
      <div className="leaderboard-modal pixel-border" onClick={(e) => e.stopPropagation()}>
        <div className="leaderboard-header">
          <h2>GLOBAL LEADERBOARD</h2>
          <button className="close-button" onClick={onClose}>
            ✕
          </button>
        </div>

        {!hasSubmitted && blendCount > 0 && (
          <div className="submit-section">
            <h3>SUBMIT YOUR SCORES</h3>
            <div className="submit-form">
              <input
                type="text"
                placeholder="ENTER YOUR NAME"
                value={playerName}
                onChange={(e) => setPlayerName(e.target.value)}
                maxLength={50}
                className="name-input"
              />
              <button onClick={handleSubmit} className="submit-button">
                SUBMIT
              </button>
            </div>
          </div>
        )}

        {hasSubmitted && (
          <div className="submit-success">
            ✓ SCORES SUBMITTED AS {playerName.toUpperCase()}!
          </div>
        )}

        <div className="system-tabs">
          {(availableSystems.length > 0 ? availableSystems : Object.keys(currentScores)).map(
            (system) => (
              <button
                key={system}
                className={`system-tab ${selectedSystem === system ? 'active' : ''}`}
                onClick={() => setSelectedSystem(system)}
              >
                {formatSystemName(system)}
              </button>
            )
          )}
        </div>

        <div className="leaderboard-content">
          {loading ? (
            <div className="loading">LOADING...</div>
          ) : entries.length === 0 ? (
            <div className="no-entries">
              <p>NO ENTRIES YET</p>
              <p className="subtitle">BE THE FIRST!</p>
            </div>
          ) : (
            <div className="entries-list">
              <div className="entries-header">
                <span className="rank-col">RANK</span>
                <span className="name-col">PLAYER</span>
                <span className="score-col">SCORE</span>
                <span className="blends-col">BLENDS</span>
              </div>
              {entries.map((entry) => (
                <div
                  key={`${entry.player_name}-${entry.achieved_at}`}
                  className={`entry-row ${entry.rank && entry.rank <= 3 ? 'top-three' : ''}`}
                >
                  <span className="rank-col">
                    {entry.rank === 1 && '🥇'}
                    {entry.rank === 2 && '🥈'}
                    {entry.rank === 3 && '🥉'}
                    {entry.rank && entry.rank > 3 && `#${entry.rank}`}
                  </span>
                  <span className="name-col">{entry.player_name}</span>
                  <span className="score-col">{entry.score.toFixed(1)}</span>
                  <span className="blends-col">{entry.blend_count}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
