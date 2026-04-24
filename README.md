# Diamond 2048

A mobile-first twist on 2048:

- The board is a **diamond** (rotated 4×4 grid) so all merges happen **diagonally**.
- Numbers start at **2048** and **halve** on each merge. Reach **2** to win.
- Swipe ↖ ↗ ↙ ↘ on mobile, or use arrow keys / WASD on desktop.

## Run it

Single file — no build step.

**On your phone (easiest):** enable GitHub Pages for this repo (Settings → Pages → deploy from `main` or this branch, root), then visit the URL on your phone.

**Local:** open `index.html` directly in a browser, or serve with `python3 -m http.server 8000` and open `http://<your-computer-ip>:8000` from your phone on the same Wi‑Fi.
