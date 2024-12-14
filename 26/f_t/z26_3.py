F = open('26-3.txt', 'r')
n = int(F.readline())
a = []
for i in range(n):
    s, f = map(int, F.readline().split())
    a.append((s, f))
a.sort(key = lambda x: x[1])
#print(a[:20])
t_prev = -1
ans = []
for i in range(n):
    if a[i][0] >= t_prev:
        t_prev = a[i][1]
        ans.append(a[i])
print(len(ans))
mx = 0
t = ans[-2][1]
for i in range(n):
    if a[i][0] >= t:
        if a[i][1] > mx:
            mx = a[i][1]
print(mx)
