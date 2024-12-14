# Автор: Д. Муфаззалов

(m, n), *a = [list(map(int, s.split())) for s in open('26-123.txt')]
ans, T, d = 0, dict(), [[] for i in range(m + 1)]
for i in sorted(a):
    for j, k in enumerate(d[i[2]]):
        if k <= i[0]:
            d[i[2]].pop(j)
            break
    else:
        ans += 1
    d[i[3]].append(i[0] + i[1])
    for j in range(i[0], i[0] + i[1]):
        T[j] = T.get(j, 0) + 1
print(ans, max(T.values()))
