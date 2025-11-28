```text
mobile-ui-integration.md

Integration steps (HTML game - recommended placement):
1. Add the markup:
   - Insert the contents of mobile-ui-overlay.html into your main index.html near the game container (for example, right below the <div id="game"> or before the closing </body>).

2. Add the CSS:
   - Link mobile-ui.css after your main stylesheet:
     <link rel="stylesheet" href="path/to/mobile-ui.css">

3. Add the JS:
   - Load mobile-touch-controls.js after your game initializes so window.game is available.
     <script src="path/to/mobile-touch-controls.js"></script>

4. Expose/Adapt game properties:
   - The script detects mode by checking window.game.mode, window.game.currentMode, or window.game.getMode().
   - Make sure the grid game and practice mode set one of those to 'grid' or 'practice'.
   - If your game stores score/lap/position under different properties, either:
     a) set window.game.score / window.game.lap / window.game.position (preferred), or
     b) edit mobile-touch-controls.js to read your actual property names.

5. Optional settings toggle:
   - To let players disable mobile HUD by default, set:
     window.settings = window.settings || {}; window.settings.mobileHudEnabled = false;

6. Mode change notification (optional but recommended):
   - If your code switches modes, dispatch a DOM event so the HUD updates immediately:
     window.dispatchEvent(new Event('game-mode-changed'));

7. Testing checklist:
   - Verify on actual touch devices (iPhone SE, mid-range Android).
   - Ensure touch zones are at least ~44px for comfortable tapping.
   - Confirm no interference with browser gestures (swipe back) or other UI elements.

If you'd like, I can:
- push these files to a branch (feature/mobile-ui-grid-practice),
- update index.html to include them,
- open a draft PR with a brief README and instructions.
```
