# Автор: Д. Муфаззалов
import itertools

with open('26-120.txt') as f:
    m, n = map(int, f.readline().split())
    b = [0] + list(itertools.accumulate(list(map(int, f.readline().split()))))
    p, ans, t = [0] * b[-1], [0] * m, [0] * m
    a = sorted([list(map(int, i.split())) for i in f])
for x, y, z in a:
    for i, j in enumerate(p[b[z]:], start=b[z]):
        if j <= x:
            p[i] = x + y
            ans[z] += 1
            t[z] = max(t[z], p[i])
            break
ans.reverse()
print(t[m - ans.index(max(ans)) - 1], n - sum(ans))