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
function initCarousel() {
  const carousel = document.getElementById('voiceCarousel');
  const track = document.getElementById('voiceTrack');
  const dots = document.querySelectorAll('.voice-dot');

  if (!carousel || !track || dots.length === 0) return;

  let currentIndex = 0;
  let startX = 0;

  function goTo(index) {
    currentIndex = Math.max(0, Math.min(index, dots.length - 1));
    if (window.innerWidth <= 768) {
      const cardWidth = carousel.offsetWidth;
      track.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
    }
    dots.forEach((dot, i) => dot.classList.toggle('active', i === currentIndex));
  }

  dots.forEach(dot => {
    dot.addEventListener('click', () => goTo(parseInt(dot.dataset.index)));
  });

  track.addEventListener('touchstart', e => {
    startX = e.touches[0].clientX;
  }, { passive: true });

  track.addEventListener('touchend', e => {
    const diff = startX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) goTo(currentIndex + (diff > 0 ? 1 : -1));
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
      track.style.transform = '';
      currentIndex = 0;
      dots.forEach((dot, i) => dot.classList.toggle('active', i === 0));
    }
  });
}
function initScrollFade() {
  const heroBg = document.querySelector('.hero-bg');
  const heroContent = document.querySelector('.hero-content');

  if (!heroBg || !heroContent) return;

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const heroHeight = document.querySelector('.hero').offsetHeight;
    if (scrollY < heroHeight) {
      heroBg.style.transform = `scale(1.05) translateY(${scrollY * 0.3}px)`;
      heroContent.style.opacity = Math.max(0, 1 - (scrollY / heroHeight) * 1.5);
    }
  }, { passive: true });
}
