# Автор: Е. Джобс

with open('26-84.txt') as f:
    n = int(f.readline())
    st = sorted([int(x) for x in f.readline().split()], reverse=True)
    au = sorted([int(x) for x in f.readline().split()], reverse=True)
c = 1
s = cm = 0
for i in range(n):
    while s < n and au[s] >= st[i]:
        s += 1
    if s == n:
        cm += 1
    c = c * (s - i) % 100000007
print(c, cm)