/**
 * API utilities for communicating with the backend
 */
import axios from 'axios';
import {
  GameObject,
  BlendResponse,
  SessionResponse,
  LeaderboardResponse,
} from '../types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Fetch session information
 */
export async function fetchSession(sessionId: string): Promise<SessionResponse> {
  const response = await api.get<SessionResponse>(`/api/scores/session/${sessionId}`);
  return response.data;
}

/**
 * Get random available objects for selection
 */
export async function getRandomObjects(
  blendCount: number,
  count: number = 3
): Promise<GameObject[]> {
  const response = await api.get<GameObject[]>(
    `/api/objects/random/${blendCount}/${count}`
  );
  return response.data;
}

/**
 * Get all available objects based on blend count
 */
export async function getAvailableObjects(blendCount: number): Promise<GameObject[]> {
  const response = await api.get<GameObject[]>(
    `/api/objects/available/${blendCount}`
  );
  return response.data;
}

/**
 * Blend objects and get results
 */
export async function blendObjects(
  sessionId: string,
  objectIds: number[]
): Promise<BlendResponse> {
  const response = await api.post<BlendResponse>('/api/scores/blend', {
    session_id: sessionId,
    object_ids: objectIds,
  });
  return response.data;
}

/**
 * Reset a session
 */
export async function resetSession(sessionId: string): Promise<void> {
  await api.post(`/api/scores/reset/${sessionId}`);
}

/**
 * Get leaderboard for a scoring system
 */
export async function getLeaderboard(
  scoringSystem: string,
  limit: number = 100
): Promise<LeaderboardResponse> {
  const response = await api.get<LeaderboardResponse>(
    `/api/leaderboard/${scoringSystem}`,
    { params: { limit } }
  );
  return response.data;
}

/**
 * Get all available leaderboards
 */
export async function getAvailableLeaderboards(): Promise<string[]> {
  const response = await api.get<string[]>('/api/leaderboard/');
  return response.data;
}

/**
 * Submit scores to leaderboard
 */
export async function submitToLeaderboard(
  sessionId: string,
  playerName: string
): Promise<void> {
  await api.post(`/api/leaderboard/submit/${sessionId}`, null, {
    params: { player_name: playerName },
  });
}
