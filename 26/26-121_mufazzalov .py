# Автор: Д. Муфаззалов

import itertools

with open('26-120.txt') as f:
    m, n = map(int, f.readline().split())
    g = list(map(int, f.readline().split()))
    b = [0] + list(itertools.accumulate(g))
    s = [w for w, e in enumerate(g) for _ in range(e)]
    p, ans, t = [0] * b[-1], [0] * m, [0] * m
    a = sorted([list(map(int, h.split())) for h in f])
    for x, y, z in a:
        for i, j in enumerate(p[b[z]:], start=b[z]):
            if j <= x:
                p[i] = x + y
                r = s[i]
                ans[r] += 1
                t[r] = max(t[r], p[i])
                break
u = max(ans)
print(t[ans.index(u)], u)
