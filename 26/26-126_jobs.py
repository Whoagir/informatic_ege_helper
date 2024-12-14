# Автор: Е. Джобс

with open('26-126.txt') as f:
    m, k, n = map(int, f.readline().split())
    s = [list(map(int, f.readline().split())) for _ in range(n)]

s.sort(key=lambda x: (x[0], -x[1]))
# на каких перегонах были свободны/заняты места
# 0 - свободно, 1 - занято
per = [[0]*k for _ in range(m+1)]
cnt = 0
for st, fn in s:
    for i in range(k):
        if per[st][i] == 0:
            cnt += 1
            for j in range(st, fn):
                per[j][i] = 1
            break

c_per = 0
for p in range(1, m+1):
    if sum(per[p]) == k:
        c_per += 1
print(cnt, c_per)
