window.addEventListener('DOMContentLoaded', () => {
  const range = document.getElementById('glowRange');
  if (range) {
    document.documentElement.style.setProperty('--glow-strength', range.value);
    range.addEventListener('input', (e) => {
      document.documentElement.style.setProperty('--glow-strength', e.target.value);
    });
  }
});
