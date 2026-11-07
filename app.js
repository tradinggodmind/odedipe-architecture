(() => {
  'use strict';
  const root = document.documentElement;
  root.classList.add('js');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const menu = document.querySelector('#navigation');
  const menuButton = document.querySelector('.menu-toggle');
  function unlock() { document.body.classList.remove('locked'); menuButton?.setAttribute('aria-expanded','false'); }
  menuButton?.addEventListener('click', () => { menu.showModal(); document.body.classList.add('locked'); menuButton.setAttribute('aria-expanded','true'); });
  menu?.querySelector('.menu-close').addEventListener('click', () => menu.close());
  menu?.addEventListener('close', unlock);
  menu?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => menu.close()));
  const cards = [...document.querySelectorAll('.project-card')];
  const grid = document.querySelector('.project-grid');
  document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => {
    document.querySelectorAll('.filter').forEach(b => b.setAttribute('aria-pressed',String(b===button)));
    const category = button.dataset.filter;
    let count = 0;
    cards.forEach(card => { card.hidden = category !== 'all' && card.dataset.category !== category; if (!card.hidden) { count++; card.classList.remove('pending'); }});
    grid.classList.toggle('filtered',category !== 'all');
    document.querySelector('.filter-status').textContent = `${String(count).padStart(2,'0')} projects`;
  }));
  if (!reduced && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.remove('pending'); observer.unobserve(entry.target); }
    }), {threshold: .06, rootMargin: '0px 0px 30px 0px'});
    document.querySelectorAll('.reveal').forEach(el => { if (el.getBoundingClientRect().top > innerHeight) {el.classList.add('pending'); observer.observe(el);} });
  }
  const lightbox = document.querySelector('#lightbox');
  if (!lightbox) return;
  const shots = [...document.querySelectorAll('[data-full]')];
  const img = lightbox.querySelector('.lightbox-image');
  const title = lightbox.querySelector('.lightbox-caption strong');
  const caption = lightbox.querySelector('.lightbox-caption span');
  const count = lightbox.querySelector('.lightbox-count');
  const zoom = lightbox.querySelector('.lightbox-zoom');
  let index = 0;
  function show(i) {
    index = (i + shots.length) % shots.length;
    const shot = shots[index];
    img.src = shot.dataset.full; img.alt = shot.dataset.alt;
    title.textContent = shot.dataset.title; caption.textContent = shot.dataset.caption;
    count.textContent = `${String(index+1).padStart(2,'0')} / ${String(shots.length).padStart(2,'0')}`;
    lightbox.classList.remove('zoomed'); zoom.textContent='View detail +'; zoom.setAttribute('aria-pressed','false');
  }
  shots.forEach((shot,i) => shot.addEventListener('click', () => { show(i); lightbox.showModal(); document.body.classList.add('locked'); }));
  lightbox.querySelector('.lightbox-close').addEventListener('click', () => lightbox.close());
  lightbox.addEventListener('close', () => {document.body.classList.remove('locked'); img.removeAttribute('src');});
  lightbox.querySelector('[data-prev]').addEventListener('click', () => show(index-1));
  lightbox.querySelector('[data-next]').addEventListener('click', () => show(index+1));
  lightbox.addEventListener('keydown', event => {if(event.key==='ArrowRight'){event.preventDefault();show(index+1)}if(event.key==='ArrowLeft'){event.preventDefault();show(index-1)}});
  zoom.addEventListener('click', () => {const on=lightbox.classList.toggle('zoomed');zoom.setAttribute('aria-pressed',String(on));zoom.textContent=on?'Fit to screen −':'View detail +';});
})();
