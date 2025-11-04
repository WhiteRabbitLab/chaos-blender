/**
 * Audio utilities for game sound effects
 */

let audioContext: AudioContext | null = null;

// Initialize audio context
const getAudioContext = (): AudioContext => {
  if (!audioContext) {
    audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
  }
  return audioContext;
};

/**
 * Generate and play a blending sound effect using Web Audio API
 * Creates a synthetic "blender" sound
 */
export function playBlendSound(): void {
  try {
    const ctx = getAudioContext();
    const now = ctx.currentTime;

    // Create oscillators for motor sound
    const oscillator1 = ctx.createOscillator();
    const oscillator2 = ctx.createOscillator();
    const oscillator3 = ctx.createOscillator();

    // Create gain nodes for volume control
    const gainNode1 = ctx.createGain();
    const gainNode2 = ctx.createGain();
    const gainNode3 = ctx.createGain();
    const masterGain = ctx.createGain();

    // Configure oscillators for motor/grinding sound
    oscillator1.type = 'sawtooth';
    oscillator1.frequency.setValueAtTime(80, now);
    oscillator1.frequency.exponentialRampToValueAtTime(120, now + 0.5);
    oscillator1.frequency.exponentialRampToValueAtTime(100, now + 1);

    oscillator2.type = 'square';
    oscillator2.frequency.setValueAtTime(160, now);
    oscillator2.frequency.exponentialRampToValueAtTime(200, now + 0.5);
    oscillator2.frequency.exponentialRampToValueAtTime(180, now + 1);

    oscillator3.type = 'triangle';
    oscillator3.frequency.setValueAtTime(40, now);
    oscillator3.frequency.exponentialRampToValueAtTime(60, now + 0.5);
    oscillator3.frequency.exponentialRampToValueAtTime(50, now + 1);

    // Configure gain envelopes
    gainNode1.gain.setValueAtTime(0, now);
    gainNode1.gain.linearRampToValueAtTime(0.1, now + 0.05);
    gainNode1.gain.exponentialRampToValueAtTime(0.05, now + 1);
    gainNode1.gain.linearRampToValueAtTime(0.001, now + 1.2);

    gainNode2.gain.setValueAtTime(0, now);
    gainNode2.gain.linearRampToValueAtTime(0.08, now + 0.05);
    gainNode2.gain.exponentialRampToValueAtTime(0.04, now + 1);
    gainNode2.gain.linearRampToValueAtTime(0.001, now + 1.2);

    gainNode3.gain.setValueAtTime(0, now);
    gainNode3.gain.linearRampToValueAtTime(0.15, now + 0.05);
    gainNode3.gain.exponentialRampToValueAtTime(0.08, now + 1);
    gainNode3.gain.linearRampToValueAtTime(0.001, now + 1.2);

    masterGain.gain.setValueAtTime(0.3, now);

    // Connect audio graph
    oscillator1.connect(gainNode1);
    oscillator2.connect(gainNode2);
    oscillator3.connect(gainNode3);

    gainNode1.connect(masterGain);
    gainNode2.connect(masterGain);
    gainNode3.connect(masterGain);

    masterGain.connect(ctx.destination);

    // Start and stop oscillators
    oscillator1.start(now);
    oscillator2.start(now);
    oscillator3.start(now);

    oscillator1.stop(now + 1.2);
    oscillator2.stop(now + 1.2);
    oscillator3.stop(now + 1.2);
  } catch (error) {
    console.error('Error playing blend sound:', error);
  }
}

/**
 * Play a success sound when unlocking new items
 */
export function playUnlockSound(): void {
  try {
    const ctx = getAudioContext();
    const now = ctx.currentTime;

    const oscillator = ctx.createOscillator();
    const gainNode = ctx.createGain();

    oscillator.type = 'sine';

    // Play ascending notes
    oscillator.frequency.setValueAtTime(523.25, now); // C5
    oscillator.frequency.setValueAtTime(659.25, now + 0.1); // E5
    oscillator.frequency.setValueAtTime(783.99, now + 0.2); // G5

    gainNode.gain.setValueAtTime(0.2, now);
    gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.4);

    oscillator.connect(gainNode);
    gainNode.connect(ctx.destination);

    oscillator.start(now);
    oscillator.stop(now + 0.4);
  } catch (error) {
    console.error('Error playing unlock sound:', error);
  }
}

/**
 * Play a selection sound when choosing objects
 */
export function playSelectSound(): void {
  try {
    const ctx = getAudioContext();
    const now = ctx.currentTime;

    const oscillator = ctx.createOscillator();
    const gainNode = ctx.createGain();

    oscillator.type = 'sine';
    oscillator.frequency.setValueAtTime(800, now);

    gainNode.gain.setValueAtTime(0.1, now);
    gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.1);

    oscillator.connect(gainNode);
    gainNode.connect(ctx.destination);

    oscillator.start(now);
    oscillator.stop(now + 0.1);
  } catch (error) {
    console.error('Error playing select sound:', error);
  }
}
