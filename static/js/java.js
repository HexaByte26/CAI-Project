// NAV BAR: hide on scroll down, show on scroll up, frosted once the page has scrolled
let lastScrollPosition = 0;
const navbar = document.querySelector('.smart-nav');

window.addEventListener('scroll', () => {
  const current = window.pageYOffset || document.documentElement.scrollTop;

  navbar.classList.toggle('nav-hidden', current > lastScrollPosition && current > 80);
  navbar.classList.toggle('nav-solid', current > 10);

  // <= 0 check prevents odd behaviour from mobile "bounce" scrolling at the very top
  lastScrollPosition = current <= 0 ? 0 : current;
});
