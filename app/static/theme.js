// Script that synchronizes the neon glow CSS variable with the slider value
window.addEventListener('DOMContentLoaded', () => {
  const range = document.getElementById('glowRange');
  if (range) {
    // Set initial value based on the slider's position
    document.documentElement.style.setProperty('--glow-strength', range.value);
    range.addEventListener('input', (e) => {
      document.documentElement.style.setProperty('--glow-strength', e.target.value);
    });
  }
});
