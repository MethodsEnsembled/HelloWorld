"""Unit tests for Facet's inverse-2048 collapse (halve on merge)."""
WIN = 2

def slide_line(vals):
    nz = [v for v in vals if v != 0]
    out = []
    merges = []
    gained = 0
    n_merges = 0
    i = 0
    while i < len(nz):
        if i + 1 < len(nz) and nz[i] == nz[i + 1] and nz[i] > WIN:
            merged = nz[i] // 2
            out.append(merged)
            gained += nz[i]
            n_merges += 1
            merges.append(len(out) - 1)
            i += 2
        else:
            out.append(nz[i])
            i += 1
    while len(out) < 4:
        out.append(0)
    return out, gained, n_merges, merges

cases = [
    ([2048, 2048, 0, 0], [1024, 0, 0, 0], 2048, 1),
    ([2048, 0, 2048, 0], [1024, 0, 0, 0], 2048, 1),
    ([2048, 2048, 2048, 2048], [1024, 1024, 0, 0], 4096, 2),
    ([2048, 2048, 2048, 0], [1024, 2048, 0, 0], 2048, 1),
    ([4, 4, 0, 0], [2, 0, 0, 0], 4, 1),
    ([2, 2, 0, 0], [2, 2, 0, 0], 0, 0),  # 2 is finished, no merge
    ([4, 2, 2, 0], [4, 2, 2, 0], 0, 0),
    ([0, 0, 0, 0], [0, 0, 0, 0], 0, 0),
    ([1024, 0, 0, 1024], [512, 0, 0, 0], 1024, 1),
    ([8, 8, 4, 4], [4, 2, 0, 0], 12, 2),
    ([16, 8, 8, 16], [16, 4, 16, 0], 8, 1),
    ([4, 0, 4, 4], [2, 4, 0, 0], 4, 1),  # first pair merges, leftover 4 stays
]

failed = 0
for src, exp, exp_g, exp_n in cases:
    got, g, n, _ = slide_line(src)
    ok = got == exp and g == exp_g and n == exp_n
    if not ok:
        failed += 1
        print("FAIL", src, "->", got, "g", g, "n", n, "expected", exp, exp_g, exp_n)
    else:
        print("ok  ", src, "->", got)

print("failed", failed, "of", len(cases))
raise SystemExit(failed)
