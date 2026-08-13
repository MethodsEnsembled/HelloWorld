"""Unit tests for Facet: inverse-2048 collapse + harvest finished 2s."""
import random

WIN = 2
SIZE = 4


def slide_line(vals):
    nz = [v for v in vals if v != 0]
    out = []
    gained = 0
    n_merges = 0
    i = 0
    while i < len(nz):
        if i + 1 < len(nz) and nz[i] == nz[i + 1] and nz[i] > WIN:
            merged = nz[i] // 2
            out.append(merged)
            gained += nz[i]
            n_merges += 1
            i += 2
        else:
            out.append(nz[i])
            i += 1
    while len(out) < SIZE:
        out.append(0)
    return out, gained, n_merges


def harvest(board):
    gems = 0
    out = [row[:] for row in board]
    for r in range(SIZE):
        for c in range(SIZE):
            if out[r][c] == WIN:
                out[r][c] = 0
                gems += 1
    return out, gems


def boards_equal(a, b):
    return all(a[r][c] == b[r][c] for r in range(SIZE) for c in range(SIZE))


def move_board(board, dir_):
    """Slide, then harvest 2s. Returns (board, gained, n_merges, gems, slid)."""
    b = [row[:] for row in board]
    if dir_ == "right":
        b = [list(reversed(r)) for r in b]
    elif dir_ == "up":
        b = [list(x) for x in zip(*b)]
    elif dir_ == "down":
        b = [list(reversed(x)) for x in zip(*b)]

    gained = 0
    n_merges = 0
    nxt = []
    for row in b:
        nr, g, n = slide_line(row)
        gained += g
        n_merges += n
        nxt.append(nr)
    b = nxt

    if dir_ == "right":
        b = [list(reversed(r)) for r in b]
    elif dir_ == "up":
        b = [list(x) for x in zip(*b)]
    elif dir_ == "down":
        b = [list(x) for x in zip(*[list(reversed(r)) for r in b])]

    slid = not boards_equal(board, b)
    b, gems = harvest(b)
    return b, gained, n_merges, gems, slid


def any_moves(board):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return True
    for r in range(SIZE):
        for c in range(SIZE):
            v = board[r][c]
            if v <= WIN:
                continue
            if c + 1 < SIZE and board[r][c + 1] == v:
                return True
            if r + 1 < SIZE and board[r + 1][c] == v:
                return True
    return False


def spawn_val(board, rng, mode, start):
    if mode == "fixed":
        return start if rng.random() < 0.9 else max(start // 2, 4)
    if mode == "half_max":
        mx = max((v for row in board for v in row), default=start)
        return max(mx // 2, 4)
    if mode == "mix":
        # 50% start, 30% start/2, 20% start/4
        x = rng.random()
        if x < 0.5:
            return start
        if x < 0.8:
            return max(start // 2, 4)
        return max(start // 4, 4)
    if mode == "facet":
        # Matches facet.html spawnValue(): 50% 2048, 25% board-min, 25% min/2.
        vals = [v for row in board for v in row if v]
        mn = min(vals) if vals else start
        x = rng.random()
        if x < 0.50:
            return start
        if x < 0.75:
            return max(mn, 4)
        return max(mn // 2, 4)
    raise ValueError(mode)


def play(seed, start=2048, mode="fixed", moves=400):
    rng = random.Random(seed)
    board = [[0] * SIZE for _ in range(SIZE)]

    def do_spawn():
        empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
        if not empty:
            return
        r, c = empty[rng.randrange(len(empty))]
        board[r][c] = spawn_val(board, rng, mode, start)

    do_spawn()
    do_spawn()
    gems = 0
    for _ in range(moves):
        if not any_moves(board):
            return gems, True
        dirs = ["left", "right", "up", "down"]
        rng.shuffle(dirs)
        moved = False
        for d in dirs:
            nxt, gained, n, g2, slid = move_board(board, d)
            if not slid and g2 == 0:
                continue
            board[:] = nxt
            gems += g2
            do_spawn()
            moved = True
            break
        if not moved:
            return gems, True
    return gems, False


SLIDE_CASES = [
    ([2048, 2048, 0, 0], [1024, 0, 0, 0], 2048, 1),
    ([2048, 0, 2048, 0], [1024, 0, 0, 0], 2048, 1),
    ([2048, 2048, 2048, 2048], [1024, 1024, 0, 0], 4096, 2),
    ([2048, 2048, 2048, 0], [1024, 2048, 0, 0], 2048, 1),
    ([4, 4, 0, 0], [2, 0, 0, 0], 4, 1),
    ([2, 2, 0, 0], [2, 2, 0, 0], 0, 0),
    ([4, 2, 2, 0], [4, 2, 2, 0], 0, 0),
    ([0, 0, 0, 0], [0, 0, 0, 0], 0, 0),
    ([1024, 0, 0, 1024], [512, 0, 0, 0], 1024, 1),
    ([8, 8, 4, 4], [4, 2, 0, 0], 12, 2),
    ([16, 8, 8, 16], [16, 4, 16, 0], 8, 1),
    ([4, 0, 4, 4], [2, 4, 0, 0], 4, 1),
]

HARVEST_CASES = [
    ([[4, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     "left",
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 1),
    ([[8, 4, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     "left",
     [[8, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 1),
    ([[4, 4, 4, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     "left",
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 2),
    ([[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     "left",
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 2),
    ([[2, 0, 8, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     "left",
     [[0, 8, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 1),
]


def main():
    failed = 0
    for src, exp, exp_g, exp_n in SLIDE_CASES:
        got, g, n = slide_line(src)
        if not (got == exp and g == exp_g and n == exp_n):
            failed += 1
            print("FAIL slide", src, "->", got, "g", g, "n", n, "expected", exp, exp_g, exp_n)
        else:
            print("ok   slide", src, "->", got)

    for src, dir_, exp, exp_gems in HARVEST_CASES:
        got, g, n, gems, slid = move_board(src, dir_)
        if not (got == exp and gems == exp_gems):
            failed += 1
            print("FAIL harvest", src, dir_, "->", got, "gems", gems)
        else:
            print("ok   harvest", dir_, "gems", gems)

    # Game spawn: 50% 2048, 25% board-min, 25% board-min/2.
    # Random play should still reach a gem sometimes; greedy play
    # (tested separately) hits far more often.
    hits = 0
    for seed in range(80):
        gems, _ = play(seed, start=2048, mode="facet")
        if gems:
            hits += 1
    print(f"facet-spawn random gems_in {hits}/80")
    if hits < 8:
        failed += 1
        print("FAIL expected facet spawn to produce gems in some random games")

    print("failed", failed)
    raise SystemExit(failed)


if __name__ == "__main__":
    main()
