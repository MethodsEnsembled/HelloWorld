---
name: verify
description: How to run and verify the games in this repo (single-file HTML, no build step).
---

# Verifying games in this repo

Every game is one self-contained HTML file at the repo root, linked from `index.html`. No build step.

## Serve

Any static server works:

```bash
python3 -m http.server 8642 --directory /path/to/repo
```

## Drive (headless)

Playwright 1.56 is installed globally (`NODE_PATH=/opt/node22/lib/node_modules`), Chromium at `/opt/pw-browsers`. Use a mobile viewport — these games are portrait, mobile-first:

```js
const ctx = await browser.newContext({ viewport: { width: 390, height: 780 }, deviceScaleFactor: 2, hasTouch: true, isMobile: true });
```

Gotchas learned the hard way:

- Big CTA buttons have infinite pulse animations — Playwright's stability check times out on them. Click with `{ force: true }`.
- Games use `pointerdown`, not `click`, for game actions; Playwright's `.click()` fires pointerdown so it works.
- Top-level `const` game state (e.g. `G` in cook-cook-chef) is a global lexical binding — readable from `page.evaluate(() => G.phase)` even though it's not on `window`. Poll phase changes with `waitForFunction` instead of sleeps.
- Collect `pageerror` and console `error` events; a run should end with zero.
- WebAudio in headless Chromium is fine (no user-gesture crash) — games init audio on first pointerdown inside a try/catch.

## What to check

Play a full session through real taps (title → game → end screen → replay), screenshot the key beats, and probe: disabled buttons, over-filling selections, sound toggle, localStorage bests surviving reload.
