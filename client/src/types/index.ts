export interface GameObject {
  id: number;
  name: string;
  category: string;
  unlock_threshold: number;
  sprite_path: string;
  scores: Record<string, number>;
  description?: string;
  rarity: string;
  color?: string;
  created_at: string;
  icon?: string;
}

export interface ScoringSystem {
  id: number;
  name: string;
  display_name: string;
  description?: string;
  unit: string;
  icon?: string;
  visible_from_start: boolean;
  created_at: string;
}

export interface BlendRequest {
  session_id: string;
  object_ids: number[];
}

export interface BlendResponse {
  success: boolean;
  blend_count: number;
  scores_added: Record<string, number>;
  total_scores: Record<string, number>;
  newly_unlocked_systems: string[];
  newly_unlocked_objects: GameObject[];
}

export interface SessionResponse {
  session_id: string;
  blend_count: number;
  scores: Record<string, number>;
  unlocked_systems: string[];
  available_objects: GameObject[];
}

export interface LeaderboardEntry {
  player_name: string;
  scoring_system: string;
  score: number;
  blend_count: number;
  achieved_at: string;
  rank?: number;
}

export interface LeaderboardResponse {
  scoring_system: string;
  entries: LeaderboardEntry[];
  total_entries: number;
}

export interface GameState {
  blendCount: number;
  scores: Record<string, number>;
  unlockedSystems: string[];
  blendedObjects: number[];
}

export interface FeedbackMessage {
  scoresAdded: Record<string, number>;
  newSystems: string[];
  newObjects: GameObject[];
}
