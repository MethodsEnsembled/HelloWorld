# Arcade

A small portal of mobile-first web games. No build step — open `index.html`.

## Games

- **2048 (Big Grid)** (`2048-big-grid.html`) — classic 2048 on any grid from 4×4 up to **300×300** (90,000 cells, still instant — flat typed-array engine plus a 1px-per-cell canvas blit). Spawning scales with the board: classic drops 1 tile per move on 16 cells, so an R×C board starts with `area/8` tiles and drops `area/16` per move — the same per-cell pressure at every size, which simulations show keeps giant boards winnable with four-direction play while two-direction corner spam still jams. Endless past 2048, smooth zoom/pan to read the numbers, a three-tier generative soundtrack (Drift → Momentum → Overdrive) that intensifies as you progress, and a shuffle button — shake your phone to trigger it.
- **TI-84 Plus CE** (`ti84.html`) — a working graphing-calculator *simulator* (not a hardware emulator — TI's OS is copyrighted, so the math engine is built from scratch). Full CE keypad with 2nd/alpha, TI-authentic evaluation quirks (token entry, `Ans` chaining, left-associative `^`), Y= graphing with window/zoom/trace/table, ▶Frac, variables, degree/radian modes, and error screens. **Writes and runs real TI-BASIC** via `prgm ▸ NEW` (Disp, Input, If/Then/Else, For, While, Repeat, Lbl/Goto, Pause), and **every key is a musical note** — the number keys play do re mi fa so la ti so you can pick out tunes like an old Casio.
- **Zero Gravity 2048** (`zero-gravity-2048.html`) — 2048 with the gravity switched off. Swipes slide and merge tiles as usual, but afterwards every tile may drift a cell across the perpendicular axis on its own — a drift that lands on a twin is a **zero-g merge worth ×2**. Rendered on one 60 fps canvas: parallax starfield, shooting stars, floating tiles, and rainbow particle explosions on every merge.
- **Zap-a-tron** (`zapatron.html`) — the powers-of-2 defense cannon, for kids who love numbers. Aliens attack with number shields; tap power cells (1, 2, 4, 8, 16, 32, 64 — one of each) that add up to the exact shield number, then FIRE. Multiplication, HALF and DOUBLE shields mix in grade-3 math, glitch waves crack a cell (two 4s instead of an 8!), combos double like the cells do, and motherships get drained weak-spot by weak-spot with visible subtraction.
- **Cook Cook Chef** (`cook-cook-chef.html`) — invented by a 4-year-old: run a restaurant for animal customers who crave meat, veggies, sweets… or (rarely) bugs. Pick 2–4 ingredients from the cooking table and they turn into real dishes — match the craving for extra gems and stars, but serve bugs to the wrong customer and they puke. Ingredients stream in 6 at a time from a basket of 30; when the basket's empty, the restaurant closes.
- **The Number Bakery** (`number-bakery.html`) — a mental-math puzzle for number-loving kids. Monster customers order a sum; drag a trail of numbered cookies that adds up exactly. Longer trails score more (rewards decomposing numbers), golden cookies double, berry cookies subtract, and every serve shows its equation.
- **Bluey & Bingo: The Big Adventure** (`bluey-adventure.html`) — a gentle one-touch runner for young kids. Pick who leads; the other pup follows and helps. Tap to jump, hold to float, munch watermelons on the way to the picnic. No game over — just stars and a sticker book.

- **Diamond 2048** (`diamond-2048.html`) — 2048 with a diamond grid; merges happen diagonally and tile values **halve** instead of doubling. Reach **2** to win.
- **Unicorn Catch** (`unicorn-catch.html`) — princesses on unicorns fall from the sky; hold and slide to catch the ones that match your pick.
- **1K Level** (`1k-level.html`) — a bouncing numbered ball smashes giant bricks down to zero. Tap to launch, flick to aim, and keep the ball off the danger platform.
- **Making Dessert** (`dessert-game.html`) — memorize the recipe, then tap the steps in order. Mess it up and the kid gets a pile of suspicious goop.
- **Pantry Panic** (`pantry-panic.html`) — a ground-up reimagining of Shelf Organization: hand-drawn SVG pantry goods, gliding drag-and-drop, and a time-chain (every match adds seconds). Chain combos, pop open boarded slots, hunt golden goods, earn stars.
- **Shelf Organization** (`shelf-organization.html`) — slide pantry items into empty spots; three in a row clears the shelf. Beat the timer as levels add deeper shelves, locked shelves, and more clutter.
- **Princess Unicorn Jump** (`princess-unicorn-jump.html`) — a real Tiny-Wings-style one-touch flyer. Hold to dive and hug the hills, release to launch off the lips. Perfect dive landings chain into rainbow fever, stars line the slopes, and each island ends at a castle — keep flying as long as you can outrace the sunset.

## Run it

**On your phone (easiest):** enable GitHub Pages on the repo (Settings → Pages → deploy from this branch, root). Visit the URL on your phone.

**Local:** open `index.html` directly, or serve with `python3 -m http.server 8000` and open `http://<your-ip>:8000` from a phone on the same Wi-Fi.
