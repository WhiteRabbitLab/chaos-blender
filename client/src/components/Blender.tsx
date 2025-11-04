import React, { useEffect, useState, useMemo } from 'react';
import { useSpring, animated, config } from 'react-spring';
import './Blender.css';
import Particles from './Particles';
import { GameObject, FeedbackMessage } from '../types';
import { playBlendSound, playUnlockSound } from '../utils/audio';
import { mixColors } from '../utils/colorMixing';

interface BlenderProps {
  selectedObjects: GameObject[];
  isBlending: boolean;
  feedbackMessage: FeedbackMessage | null;
}

function Blender({ selectedObjects, isBlending, feedbackMessage }: BlenderProps) {
  const [showParticles, setShowParticles] = useState(false);
  const [persistedColor, setPersistedColor] = useState<string | null>(null);

  // Calculate mixed color from selected objects AND existing color
  const mixedColor = useMemo(() => {
    const newColors = selectedObjects
      .map(obj => obj.color)
      .filter((color): color is string => color !== undefined && color !== null);

    if (newColors.length === 0) {
      return null;
    }

    // If there's already a color in the blender, include it in the mix
    const allColors = persistedColor ? [persistedColor, ...newColors] : newColors;

    return mixColors(allColors);
  }, [selectedObjects, persistedColor]);

  // Update persisted color when blending starts (while we still have the objects)
  useEffect(() => {
    if (isBlending && mixedColor) {
      // Blending just started - save the color that will be the result
      setPersistedColor(mixedColor);
    }
  }, [isBlending, mixedColor]);

  // Display color - use current mixed color or fall back to persisted color
  const displayColor = mixedColor || persistedColor;

  // Blender shake animation when blending
  const blenderSpring = useSpring({
    transform: isBlending
      ? 'rotate(0deg)'
      : 'rotate(0deg)',
    config: config.wobbly,
  });

  // Show particles and play sound when blending
  useEffect(() => {
    if (isBlending) {
      setShowParticles(true);
      playBlendSound();
      // Hide particles after animation
      const timer = setTimeout(() => {
        setShowParticles(false);
      }, 1500);
      return () => clearTimeout(timer);
    }
  }, [isBlending]);

  // Play unlock sound when new items are unlocked
  useEffect(() => {
    if (feedbackMessage && (feedbackMessage.newSystems.length > 0 || feedbackMessage.newObjects.length > 0)) {
      playUnlockSound();
    }
  }, [feedbackMessage]);

  return (
    <div className="blender-container">
      <animated.div className="blender" style={blenderSpring}>
        <div className={`blender-jar ${isBlending ? 'blending' : ''}`}>
          {/* Color liquid layer */}
          {displayColor && (
            <div
              className={`blender-liquid ${isBlending ? 'mixing' : ''}`}
              style={{
                backgroundColor: displayColor,
                opacity: isBlending ? 0.7 : 0.5,
              }}
            />
          )}

          {/* Blender contents */}
          <div className="blender-contents">
            {selectedObjects.map((obj, index) => (
              <div
                key={obj.id}
                className={`selected-object-preview ${isBlending ? 'mixing' : ''}`}
                style={{
                  animationDelay: `${index * 0.1}s`,
                }}
              >
                <img src={obj.sprite_path} alt={obj.name} className="object-sprite" />
                <span className="object-name">{obj.name}</span>
              </div>
            ))}
          </div>

          {/* Blade */}
          <div className={`blender-blade ${isBlending ? 'spinning' : ''}`}>
            <div className="blade"></div>
          </div>
        </div>

        {/* Blender base */}
        <div className="blender-base">
          <div className="blender-buttons">
            <div className={`power-light ${isBlending ? 'active' : ''}`}></div>
          </div>
        </div>
      </animated.div>

      {/* Particles effect */}
      {showParticles && <Particles />}
    </div>
  );
}

export default Blender;
