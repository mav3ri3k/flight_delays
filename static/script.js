// optional: smooth-scroll result into view
document.getElementById('delayForm')?.addEventListener('submit', () => {
  setTimeout(() => {
    document.querySelector('.result')?.scrollIntoView({ behavior: 'smooth' });
  }, 100);
});

