import React from 'react';
import './ObjectSelection.css';
import { GameObject } from '../types';
import { playSelectSound } from '../utils/audio';

interface ObjectSelectionProps {
  objects: GameObject[];
  selectedObjects: GameObject[];
  onSelect: (obj: GameObject) => void;
  requiredSelection: number;
}

function ObjectSelection({ objects, selectedObjects, onSelect, requiredSelection }: ObjectSelectionProps) {
  const isSelected = (obj: GameObject) => {
    return selectedObjects.some(selected => selected.id === obj.id);
  };

  const canSelect = (obj: GameObject) => {
    if (isSelected(obj)) return true;
    return selectedObjects.length < requiredSelection;
  };

  // Get sprite path for object
  const getSpritePath = (obj: GameObject): string => {
    return obj.sprite_path;
  };

  // Get rarity color
  const getRarityColor = (rarity: string): string => {
    const colors: Record<string, string> = {
      common: '#ffffff',
      uncommon: '#00ff00',
      rare: '#3a86ff',
      epic: '#8338ec',
      legendary: '#ff006e',
    };
    return colors[rarity] || '#ffffff';
  };

  // Handle object selection with sound
  const handleSelect = (obj: GameObject) => {
    if (canSelect(obj)) {
      playSelectSound();
      onSelect(obj);
    }
  };

  return (
    <div className="object-selection">
      <div className="selection-header">
        <h2>
          SELECT {requiredSelection} OBJECT{requiredSelection > 1 ? 'S' : ''}
        </h2>
        <p className="selection-count">
          {selectedObjects.length} / {requiredSelection} SELECTED
        </p>
      </div>

      <div className="objects-grid">
        {objects.map((obj) => (
          <div
            key={obj.id}
            className={`object-card pixel-border ${isSelected(obj) ? 'selected' : ''} ${!canSelect(obj) ? 'disabled' : ''}`}
            onClick={() => handleSelect(obj)}
            style={{
              borderColor: getRarityColor(obj.rarity),
            }}
          >
            <div className="object-icon">
              <img src={getSpritePath(obj)} alt={obj.name} className="sprite-image" />
            </div>
            <div className="object-info">
              <h3 className="object-name">{obj.name}</h3>
              <p className="object-description">{obj.description}</p>
            </div>
            {isSelected(obj) && (
              <div className="selected-indicator">✓</div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default ObjectSelection;
