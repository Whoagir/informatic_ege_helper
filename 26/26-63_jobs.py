# Автор: Е. Джобс

target = 'Z'
with open('26-62.txt') as f:
    n, m = map(int, f.readline().split())
    ds = []
    for s in f:
        p, t = s.split()
        p = int(p)
        ds.append((p, t))

ds.sort(key=lambda x: (x[0], x[1] != target))

ind = c = 0
for mx, d in enumerate(ds):
    if d[0] <= m:
        m -= d[0]
        ind = c = mx + 1
    else:
        break

for p, t in ds[ind:]:
    if t == target:
        ind -= 1
        while ind >= 0 and (ds[ind][1] == target or p - ds[ind][0] > m):
            c -= ds[ind][1] != target
            ind -= 1
        if ind >= 0:
            m -= p - ds[ind][0]
        else:
            break
print(c, m)