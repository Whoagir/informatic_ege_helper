F = open('26-1.txt', 'r')
n, L, m = map(int, F.readline().split())
a = []
for i in range(n):
    x, y, z = F.readline().split()
    a.append((int(x), int(x) + int(y), z))
a.sort()
cnt_m = 0
cnt_l =0
pa = [-1] * L # парковка а/м
pm = [-1] * m # парковка m/a
for i in range(n):
    fl = False
    if a[i][2] == 'A':
        for j in range(L):
            if a[i][0] >= pa[j]:
                pa[j] = a[i][1]
                fl = True
                break
        if not fl:
            for j in range(m):
                if a[i][0] >= pm[j]:
                    pm[j] = a[i][1]
                    fl = True
                    break
    else:
        for j in range(m):
            if a[i][0] >= pm[j]:
                pm[j] = a[i][1]
                fl = True
                break
        if fl:
            cnt_m += 1
    if not fl:
        cnt_l += 1
print(cnt_m, cnt_l)
