# Автор: Е. Джобс

with open('26-97.txt') as f:
    n = int(f.readline())
    trs = []
    for _ in range(n):
        d, s = map(int, f.readline().split())
        trs.append( (d-2*s-3, d, s) )

trs.sort(reverse=True)

pck = [trs[0]]
for tr in trs:
    if tr[1] <= pck[-1][0]:
        pck.append(tr)

max_d = 0
for tr in trs:
    if tr[1] <= pck[-2][0]:
        max_d = max(max_d, tr[1])
print(len(pck), max_d)

