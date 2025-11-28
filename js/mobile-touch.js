// mobile-touch-controls.js
// Attach this after your game initializes. It will:
// - show mobile HUD only if window.game && game.mode is 'grid' or 'practice'
// - update HUD values if window.game exposes score/lap/position (hooks included)
// - dispatch custom events for input: mobile-left-start, mobile-left-end, mobile-right-start, ...
(function () {
  const ALLOWED_MODES = ['grid', 'practice'];

  function isTouchDevice() {
    return ('ontouchstart' in window) || navigator.maxTouchPoints > 0 || navigator.msMaxTouchPoints > 0;
  }

  function currentModeIsAllowed() {
    try {
      const mode = window.game && (window.game.mode || window.game.currentMode || window.game.getMode && window.game.getMode());
      if (!mode) return false;
      return ALLOWED_MODES.includes(String(mode).toLowerCase());
    } catch (e) { return false; }
  }

  function initMobileUI() {
    const hud = document.getElementById('mobile-hud');
    if (!hud) return;
    if (!isTouchDevice() || !currentModeIsAllowed()) {
      hud.style.display = 'none';
      hud.setAttribute('aria-hidden', 'true');
      return;
    }
    hud.style.display = '';
    hud.setAttribute('aria-hidden', 'false');
    // mark playing if game state indicates active play to allow translucency
    if (window.game && window.game.isPlaying) {
      hud.classList.add('playing');
    } else {
      hud.classList.remove('playing');
    }
    hookButtons();
    startHudUpdater();
  }

  function makeButton(id, eventName) {
    const el = document.getElementById(id);
    if (!el) return;
    let active = false;
    const start = (e) => { if (e && e.preventDefault) e.preventDefault(); if (active) return; active = true; window.dispatchEvent(new CustomEvent(eventName + '-start')); el.classList.add('active'); };
    const end = (e) => { if (!active) return; active = false; window.dispatchEvent(new CustomEvent(eventName + '-end')); el.classList.remove('active'); };
    el.addEventListener('touchstart', start, {passive:false});
    el.addEventListener('mousedown', start);
    ['touchend','touchcancel','mouseup','mouseleave'].forEach(evt => el.addEventListener(evt, end));
  }

  function hookButtons() {
    makeButton('btn-left', 'mobile-left');
    makeButton('btn-right', 'mobile-right');
    makeButton('btn-boost', 'mobile-boost');
    makeButton('btn-jump', 'mobile-jump');

    // Example mapping: if your game has an input manager, wire events into it.
    // Adjust the mapping to your game's API (input manager, player controller, etc.)
    window.addEventListener('mobile-left-start', () => {
      if (window.game && window.game.input) window.game.input.set && window.game.input.set('left', true);
    });
    window.addEventListener('mobile-left-end', () => {
      if (window.game && window.game.input) window.game.input.set && window.game.input.set('left', false);
    });
    window.addEventListener('mobile-right-start', () => {
      if (window.game && window.game.input) window.game.input.set && window.game.input.set('right', true);
    });
    window.addEventListener('mobile-right-end', () => {
      if (window.game && window.game.input) window.game.input.set && window.game.input.set('right', false);
    });
    window.addEventListener('mobile-boost-start', () => {
      if (window.game && window.game.input) window.game.input.set && window.game.input.set('boost', true);
    });
    window.addEventListener('mobile-boost-end', () => {
      if (window.game && window.game.input) window.game.input.set && window.game.input.set('boost', false);
    });
    window.addEventListener('mobile-jump-start', () => {
      if (window.game && window.game.input) window.game.input.set && window.game.input.set('jump', true);
    });
    window.addEventListener('mobile-jump-end', () => {
      if (window.game && window.game.input) window.game.input.set && window.game.input.set('jump', false);
    });
  }

  // HUD updater: try to read values from window.game and update the DOM.
  let hudInterval = null;
  function startHudUpdater() {
    if (hudInterval) return;
    hudInterval = setInterval(() => {
      try {
        const scoreEl = document.getElementById('hud-score-val');
        const lapEl = document.getElementById('hud-lap-val');
        const posEl = document.getElementById('hud-pos');
        if (window.game) {
          if (scoreEl && (window.game.score !== undefined)) scoreEl.textContent = window.game.score;
          if (lapEl && (window.game.lap !== undefined)) lapEl.textContent = window.game.lap;
          if (posEl && (window.game.position !== undefined)) posEl.textContent = window.game.positionLabel || window.game.position;
        }
      } catch (e) { /* ignore */ }
    }, 150); // update ~6-7 times per second (tweak as needed)
  }

  function stopHudUpdater() {
    if (hudInterval) { clearInterval(hudInterval); hudInterval = null; }
  }

  // Re-check on focus and when game mode changes (if game fires an event)
  window.addEventListener('load', initMobileUI);
  window.addEventListener('resize', initMobileUI);
  window.addEventListener('orientationchange', initMobileUI);
  window.addEventListener('focus', initMobileUI);

  // If your game triggers a custom event when mode changes, hook it here:
  window.addEventListener('game-mode-changed', initMobileUI);

  // Expose a manual init for integration: call window.MobileUI && window.MobileUI.init()
  window.MobileUI = {
    init: initMobileUI,
    stop: () => { stopHudUpdater(); const hud = document.getElementById('mobile-hud'); if (hud) { hud.style.display = 'none'; hud.setAttribute('aria-hidden', 'true'); } }
  };

  // Try to init right now
  initMobileUI();
})();
