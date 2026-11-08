(() => {
  'use strict';

  const root = document.documentElement;
  const loader = document.querySelector('#site-loader');
  if (!loader) return;
  if (!root.classList.contains('is-loading')) {
    loader.remove();
    return;
  }

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const started = Number(root.dataset.loaderStarted) || performance.now();
  const minimum = reduced ? 0 : 1300;
  const track = loader.querySelector('.loader-track');
  const bar = loader.querySelector('.loader-bar');
  const counter = loader.querySelector('[data-loader-count]');
  let target = 0;
  let shown = 0;
  let lastNumber = -1;
  let completed = 0;
  let finishing = false;
  let frame = 0;
  let deadline = 0;
  let revealTimer = 0;
  let cleanupTimer = 0;

  function progress(value) {
    if (value === lastNumber) return;
    lastNumber = value;
    counter.textContent = String(value);
    track.setAttribute('aria-valuenow', String(value));
    bar.style.transform = 'scaleX(' + value / 100 + ')';
  }

  function cleanup() {
    window.cancelAnimationFrame(frame);
    window.clearTimeout(deadline);
    window.clearTimeout(revealTimer);
    window.clearTimeout(cleanupTimer);
    root.classList.remove('is-loading', 'is-opening');
    delete root.dataset.loaderStarted;
    loader.remove();
  }

  function finish() {
    if (finishing) return;
    finishing = true;
    window.cancelAnimationFrame(frame);
    window.clearTimeout(deadline);
    if (!root.classList.contains('is-loading')) {
      cleanup();
      return;
    }
    progress(100);
    revealTimer = window.setTimeout(() => {
      root.classList.add('is-opening');
      root.classList.remove('is-loading');
      loader.setAttribute('aria-hidden', 'true');
      cleanupTimer = window.setTimeout(cleanup, reduced ? 0 : 760);
    }, reduced ? 0 : 160);
  }

  function imageReady(image) {
    if (!image) return Promise.resolve();
    function decode() {
      return image.naturalWidth && image.decode
        ? image.decode().catch(() => {})
        : Promise.resolve();
    }
    if (image.complete) return decode();
    return new Promise(resolve => {
      function settle() {
        image.removeEventListener('load', settle);
        image.removeEventListener('error', settle);
        decode().then(resolve, resolve);
      }
      image.addEventListener('load', settle, { once: true });
      image.addEventListener('error', settle, { once: true });
    });
  }

  // Only the opening image and the two display/UI fonts gate the reveal.
  // Lower-page photographs retain their existing native lazy loading.
  const tasks = [
    { weight: 25, promise: document.fonts ? document.fonts.load('16px Instrument') : Promise.resolve() },
    { weight: 15, promise: document.fonts ? document.fonts.load('16px Work') : Promise.resolve() },
    { weight: 60, promise: imageReady(document.querySelector('img[loading="eager"]')) }
  ];
  tasks.forEach(task => {
    function settle() {
      target += task.weight;
      completed++;
    }
    Promise.resolve(task.promise).then(settle, settle);
  });

  function draw(now) {
    // Also respects the independent head-script timeout if the main file was late.
    if (!root.classList.contains('is-loading')) {
      cleanup();
      return;
    }
    shown += (target - shown) * 0.1;
    progress(Math.min(99, Math.floor(shown)));
    if (completed === tasks.length && now - started >= minimum) {
      finish();
    } else {
      frame = window.requestAnimationFrame(draw);
    }
  }

  deadline = window.setTimeout(finish, Math.max(0, 6000 - (performance.now() - started)));
  frame = window.requestAnimationFrame(draw);
  window.addEventListener('pageshow', event => {
    if (event.persisted) cleanup();
  });
})();
