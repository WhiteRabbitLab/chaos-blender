import React, { useState, useEffect } from 'react';
import './App.css';
import Blender from './components/Blender';
import ObjectSelection from './components/ObjectSelection';
import ScoreDisplay from './components/ScoreDisplay';
import Leaderboard from './components/Leaderboard';
import GameHeader from './components/GameHeader';
import { getSessionId } from './utils/session';
import { fetchSession, blendObjects, getRandomObjects } from './utils/api';
import { GameObject, FeedbackMessage } from './types';

function App() {
  const [sessionId, setSessionId] = useState(getSessionId());
  const [gameState, setGameState] = useState({
    blendCount: 0,
    scores: {} as Record<string, number>,
    unlockedSystems: [] as string[],
    blendedObjects: [] as number[]
  });
  const [availableObjects, setAvailableObjects] = useState<GameObject[]>([]);
  const [selectedObjects, setSelectedObjects] = useState<GameObject[]>([]);
  const [isBlending, setIsBlending] = useState(false);
  const [showLeaderboard, setShowLeaderboard] = useState(false);
  const [feedbackMessage, setFeedbackMessage] = useState<FeedbackMessage | null>(null);

  // Load session on mount
  useEffect(() => {
    loadSession();
  }, [sessionId]);

  // Load available objects when blend count changes
  useEffect(() => {
    if (gameState.blendCount !== null) {
      loadRandomObjects();
    }
  }, [gameState.blendCount]);

  const loadSession = async () => {
    try {
      const session = await fetchSession(sessionId);
      setGameState({
        blendCount: session.blend_count,
        scores: session.scores,
        unlockedSystems: session.unlocked_systems,
        blendedObjects: []
      });
    } catch (error) {
      console.error('Error loading session:', error);
    }
  };

  const loadRandomObjects = async () => {
    try {
      const count = gameState.blendCount === 0 ? 3 : 3;
      const objects = await getRandomObjects(gameState.blendCount, count);
      setAvailableObjects(objects);
    } catch (error) {
      console.error('Error loading objects:', error);
    }
  };

  const handleObjectSelect = (object: GameObject) => {
    // First blend: select 2 objects
    // Subsequent blends: select 1 object
    const maxSelection = gameState.blendCount === 0 ? 2 : 1;

    if (selectedObjects.find(obj => obj.id === object.id)) {
      // Deselect
      setSelectedObjects(selectedObjects.filter(obj => obj.id !== object.id));
    } else if (selectedObjects.length < maxSelection) {
      // Select
      setSelectedObjects([...selectedObjects, object]);
    }
  };

  const handleBlend = async () => {
    const requiredSelection = gameState.blendCount === 0 ? 2 : 1;
    if (selectedObjects.length !== requiredSelection) {
      return;
    }

    // Clear previous feedback when starting a new blend
    setFeedbackMessage(null);
    setIsBlending(true);

    try {
      const result = await blendObjects(sessionId, selectedObjects.map(obj => obj.id));

      // Show feedback message
      const feedback = {
        scoresAdded: result.scores_added,
        newSystems: result.newly_unlocked_systems,
        newObjects: result.newly_unlocked_objects
      };
      setFeedbackMessage(feedback);

      // Update game state
      setGameState({
        blendCount: result.blend_count,
        scores: result.total_scores,
        unlockedSystems: Object.keys(result.total_scores),
        blendedObjects: [...gameState.blendedObjects, ...selectedObjects.map(obj => obj.id)]
      });

      // Clear selection
      setSelectedObjects([]);

    } catch (error) {
      console.error('Error blending:', error);
      alert('Failed to blend objects. Please try again.');
    } finally {
      setTimeout(() => {
        setIsBlending(false);
      }, 1500);
    }
  };

  const handleReset = () => {
    if (window.confirm('Are you sure you want to reset your game?')) {
      // Generate new session
      const newSessionId = `session-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
      localStorage.setItem('chaos_blender_session', newSessionId);
      setSessionId(newSessionId);
      setGameState({
        blendCount: 0,
        scores: {},
        unlockedSystems: [],
        blendedObjects: []
      });
      setSelectedObjects([]);
      setFeedbackMessage(null);
    }
  };

  const requiredSelection = gameState.blendCount === 0 ? 2 : 1;
  const canBlend = selectedObjects.length === requiredSelection && !isBlending;

  return (
    <div className="App">
      <GameHeader
        blendCount={gameState.blendCount}
        onShowLeaderboard={() => setShowLeaderboard(true)}
        onReset={handleReset}
      />

      <div className="game-container">
        <div className="left-panel">
          <div className="info-panel pixel-border">
            <h3>HOW TO PLAY</h3>
            <div className="info-content">
              <p>
                {gameState.blendCount === 0
                  ? '1. SELECT 2 OBJECTS'
                  : '1. SELECT 1 OBJECT'
                }
              </p>
              <p>2. CLICK BLEND IT!</p>
              <p>3. EARN POINTS</p>
              <p>4. UNLOCK NEW ITEMS</p>
            </div>
          </div>

          {/* Feedback message */}
          {feedbackMessage && (
            <div className="blend-feedback pixel-border">
              <h3>BLEND COMPLETE!</h3>
              {feedbackMessage.newSystems.length > 0 && (
                <div className="feedback-section">
                  <p className="feedback-highlight">
                    🎉 NEW SYSTEMS UNLOCKED!
                  </p>
                  {feedbackMessage.newSystems.map((system) => (
                    <p key={system} className="feedback-item">
                      ✨ {system.replace(/_/g, ' ').toUpperCase()}
                    </p>
                  ))}
                </div>
              )}
              {feedbackMessage.newObjects.length > 0 && (
                <div className="feedback-section">
                  <p className="feedback-highlight">
                    🔓 NEW OBJECTS UNLOCKED!
                  </p>
                  {feedbackMessage.newObjects.map((obj) => (
                    <p key={obj.id} className="feedback-item">
                      ⭐ {obj.name}
                    </p>
                  ))}
                </div>
              )}
              <div className="feedback-section">
                <p className="feedback-label">POINTS EARNED:</p>
                {Object.entries(feedbackMessage.scoresAdded).map(([system, value]) => (
                  <p key={system} className="feedback-score">
                    {system.replace(/_/g, ' ').toUpperCase()}: +{value.toFixed(1)}
                  </p>
                ))}
              </div>
            </div>
          )}
        </div>

        <div className="center-panel">
          <Blender
            selectedObjects={selectedObjects}
            isBlending={isBlending}
            feedbackMessage={feedbackMessage}
          />

          <ObjectSelection
            objects={availableObjects}
            selectedObjects={selectedObjects}
            onSelect={handleObjectSelect}
            requiredSelection={requiredSelection}
          />

          <button
            className="blend-button"
            onClick={handleBlend}
            disabled={!canBlend}
          >
            {isBlending ? 'BLENDING...' : 'BLEND IT!'}
          </button>
        </div>

        <div className="right-panel">
          <ScoreDisplay
            scores={gameState.scores}
            unlockedSystems={gameState.unlockedSystems}
          />
        </div>
      </div>

      {showLeaderboard && (
        <Leaderboard
          sessionId={sessionId}
          currentScores={gameState.scores}
          blendCount={gameState.blendCount}
          onClose={() => setShowLeaderboard(false)}
        />
      )}
    </div>
  );
}

export default App;
