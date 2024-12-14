# Автор: Д. Муфаззалов

with open('26-92.txt') as f:
    d = {}
    for i in range(int(f.readline())):
        s = f.readline().split()
        d[tuple(map(int, s[:2]))] = int(s[-1] == '+')
b = sorted(d)
x = m = d[b[0]]
j = b[0][0]
for i in range(1, len(d)):
    if b[i][0] == b[i - 1][0] and d[b[i]] and b[i][1] == b[i - 1][1] + 1:
        x += 1
        if x >= m:
            m, j = max(x, m), b[i][0]
    else:
        x = d[b[0]]
print(m, j)