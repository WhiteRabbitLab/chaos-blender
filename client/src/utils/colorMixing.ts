/**
 * Color mixing utilities using RGB color theory
 */

/**
 * Converts a hex color to RGB values
 */
export function hexToRgb(hex: string): { r: number; g: number; b: number } | null {
  // Remove # if present
  const cleanHex = hex.replace('#', '');

  // Parse hex string
  const bigint = parseInt(cleanHex, 16);
  const r = (bigint >> 16) & 255;
  const g = (bigint >> 8) & 255;
  const b = bigint & 255;

  return { r, g, b };
}

/**
 * Converts RGB values to hex color
 */
export function rgbToHex(r: number, g: number, b: number): string {
  const toHex = (n: number) => {
    const hex = Math.round(n).toString(16);
    return hex.length === 1 ? '0' + hex : hex;
  };

  return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

/**
 * Mixes multiple hex colors using RGB averaging
 * This simulates subtractive color mixing (like mixing paints)
 */
export function mixColors(hexColors: string[]): string {
  if (hexColors.length === 0) {
    return '#FFFFFF'; // Default to white if no colors
  }

  if (hexColors.length === 1) {
    return hexColors[0];
  }

  // Convert all hex colors to RGB
  const rgbColors = hexColors
    .map(hex => hexToRgb(hex))
    .filter((rgb): rgb is { r: number; g: number; b: number } => rgb !== null);

  if (rgbColors.length === 0) {
    return '#FFFFFF';
  }

  // Calculate average RGB values (simple averaging for realistic color mixing)
  const avgR = rgbColors.reduce((sum, rgb) => sum + rgb.r, 0) / rgbColors.length;
  const avgG = rgbColors.reduce((sum, rgb) => sum + rgb.g, 0) / rgbColors.length;
  const avgB = rgbColors.reduce((sum, rgb) => sum + rgb.b, 0) / rgbColors.length;

  // Convert back to hex
  return rgbToHex(avgR, avgG, avgB);
}

/**
 * Lighten or darken a color by a percentage
 * @param hex - The hex color to adjust
 * @param percent - Positive to lighten, negative to darken (-100 to 100)
 */
export function adjustBrightness(hex: string, percent: number): string {
  const rgb = hexToRgb(hex);
  if (!rgb) return hex;

  const adjust = (value: number) => {
    const adjusted = value + (value * percent / 100);
    return Math.max(0, Math.min(255, adjusted));
  };

  return rgbToHex(adjust(rgb.r), adjust(rgb.g), adjust(rgb.b));
}

/**
 * Get a gradient of colors between the mixed colors
 * Useful for particle effects
 */
export function getColorGradient(hexColors: string[], steps: number = 3): string[] {
  if (hexColors.length === 0) return ['#FFFFFF'];
  if (hexColors.length === 1) return [hexColors[0]];

  const gradient: string[] = [];

  for (let i = 0; i < hexColors.length - 1; i++) {
    const start = hexToRgb(hexColors[i]);
    const end = hexToRgb(hexColors[i + 1]);

    if (!start || !end) continue;

    for (let step = 0; step < steps; step++) {
      const ratio = step / steps;
      const r = start.r + (end.r - start.r) * ratio;
      const g = start.g + (end.g - start.g) * ratio;
      const b = start.b + (end.b - start.b) * ratio;

      gradient.push(rgbToHex(r, g, b));
    }
  }

  // Add the final color
  gradient.push(hexColors[hexColors.length - 1]);

  return gradient;
}
