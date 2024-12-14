# Автор: Г.М. Федченко

f = open('26-112.txt')
n, m = map(int, f.readline().split())
a = [tuple(map(int, line.split())) for line in f]
a = sorted(a, key=lambda x: x[0])

free = [0] * n
cnt = [0] * n
maxstart = 0

for start, time in a:
    if start < 24 * 60:
        # ищем свободный банкомат
        for i in range(n):
            if free[i] < start:
                maxstart = max(maxstart, start)
                free[i] = start + time
                cnt[i] += 1
                break
        else:
        # иначе ищем тот банкомат, который освободится раньше других
            i = free.index(min(free))
            if free[i] < 24 * 60:
                maxstart = max(maxstart, free[i])
                free[i] += time
                cnt[i] += 1

print(max(cnt), maxstart)