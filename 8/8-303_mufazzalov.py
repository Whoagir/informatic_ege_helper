# Автор: Д. Муфаззалов

def f(i, ps, pg):
    if i == 6: return 7
    ans = 0
    for j in g[g.index(pg):]:
        ans += f(i + 1, ps, j)
    for j in s[s.index(ps):]:
        ans += f(i + 1, j, pg)
    return ans


g, s = sorted('АИУОЯ'), sorted('НТП', reverse=True)
print(f(0, max(s), min(g)))


# /////////////////////////////////////////

def f(i, ps, pg):
    if i == 6: return 7
    ans = sum([f(i + 1, ps, j) for j in range(pg, 5)])
    ans += sum([f(i + 1, j, pg) for j in range(ps, 3)])
    return ans


print(f(0, 0, 0))
