import React from 'react';
import './ScoreDisplay.css';

interface ScoreDisplayProps {
  scores: Record<string, number>;
  unlockedSystems: string[];
}

function ScoreDisplay({ scores, unlockedSystems }: ScoreDisplayProps) {
  // Scoring system display names and icons
  const systemInfo: Record<string, { display: string; icon: string; unit: string }> = {
    nutritional_value: { display: 'Nutritional Value', icon: '🥗', unit: 'vitamins' },
    impossibility_index: { display: 'Impossibility Index', icon: '🌀', unit: 'paradoxes' },
    awful_colour: { display: 'Awful Colour', icon: '🎨', unit: 'yikes' },
    deep_lore: { display: 'Deep Lore', icon: '📜', unit: 'secrets' },
    gift_quality: { display: 'Gift Quality', icon: '🎁', unit: 'regrets avoided' },
    chaos_energy: { display: 'Chaos Energy', icon: '⚡', unit: 'entropy' },
    temporal_displacement: { display: 'Temporal Displacement', icon: '⏰', unit: 'chrono-wobbles' },
    existential_dread: { display: 'Existential Dread', icon: '👁️', unit: 'void stares' },
    aesthetic_vibes: { display: 'Aesthetic Vibes', icon: '✨', unit: 'vibes' },
    forbidden_power: { display: 'Forbidden Power', icon: '🔮', unit: 'elder souls' },
  };

  // Get color based on score value
  const getScoreColor = (value: number): string => {
    if (value < 0) return '#ff006e';
    if (value < 50) return '#3a86ff';
    if (value < 100) return '#8338ec';
    if (value < 200) return '#ffbe0b';
    return '#00ff00';
  };

  return (
    <div className="score-display">
      <h2 className="scores-title">YOUR SCORES</h2>

      {unlockedSystems.length === 0 ? (
        <div className="no-scores pixel-border">
          <p>START BLENDING</p>
        </div>
      ) : (
        <div className="scores-list">
          {unlockedSystems.map((system) => {
            const value = scores[system] || 0;
            const info = systemInfo[system] || {
              display: system.replace(/_/g, ' ').toUpperCase(),
              icon: '❓',
              unit: 'points',
            };

            return (
              <div key={system} className="score-item pixel-border">
                <div className="score-header">
                  <span className="score-icon">{info.icon}</span>
                  <h3 className="score-name">{info.display}</h3>
                </div>
                <div className="score-value-container">
                  <span
                    className="score-value"
                    style={{ color: getScoreColor(value) }}
                  >
                    {value.toFixed(1)}
                  </span>
                  <span className="score-unit">{info.unit}</span>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default ScoreDisplay;
