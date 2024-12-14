# Автор: Е. Джобс

with open('26-124.txt') as f:
    k, m, n = map(int, f.readline().split())
    q = [int(f.readline()) for _ in range(n)]

q.sort(reverse=1)
free = [m]*k
cnt = 0
for x in q:
    for i in range(k):
        if free[i] >= x:
            free[i] -= x
            cnt += 1
            break
print(cnt, sum(free))


