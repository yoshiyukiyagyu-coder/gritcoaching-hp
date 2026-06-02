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
  });

  menuBtn.addEventListener('click', () => {
    nav.classList.toggle('open');
  });

  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => nav.classList.remove('open'));
  });
}
function initCarousel() {}
function initScrollFade() {}
