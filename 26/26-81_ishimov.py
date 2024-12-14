# Автор: М. Ишимов

f = open('26-81.txt')
n, k = map(int, f.readline().split())
a1 = [[] for x in range(100001)]
a2 = [[] for x in range(100001)]
ans = []

for i in range(n):
    e, r, m = map(int, f.readline().split())
    if e == 1:
        a1[r].append(m)
    elif e == 2:
        a2[r].append(m)

for r in range(100001):
    a1[r].sort()
    mas = sorted(a1[r])
    for m in range(1, len(mas)):
        if mas[m] - mas[m - 1] - 1 == 4:
            ans.append( (r, 1) )

    a2[r].sort()
    mas = sorted(a2[r])
    for m in range(1, len(mas)):
        if mas[m] - mas[m - 1] - 1 == 4:
            ans.append( (r, 2) )


print(max(ans, key = lambda x: x[0])[0], len(ans))