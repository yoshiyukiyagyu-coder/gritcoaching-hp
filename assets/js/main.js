document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initCarousel();
  initScrollFade();
});

function initHeader() {
  const header = document.getElementById('site-header');
  const menuBtn = header.querySelector('.header-menu-btn');
  const nav = header.querySelector('.header-nav');

  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 50);
  }, { passive: true });

  menuBtn.addEventListener('click', () => {
    nav.classList.toggle('open');
  });

  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => nav.classList.remove('open'));
  });
}
function initCarousel() {}
function initScrollFade() {
  const heroBg = document.querySelector('.hero-bg');
  const heroContent = document.querySelector('.hero-content');

  if (!heroBg) return;

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const heroHeight = document.querySelector('.hero').offsetHeight;
    if (scrollY < heroHeight) {
      heroBg.style.transform = `scale(1.05) translateY(${scrollY * 0.3}px)`;
      heroContent.style.opacity = 1 - (scrollY / heroHeight) * 1.5;
    }
  }, { passive: true });
}
