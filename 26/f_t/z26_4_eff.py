F = open('26-4.txt')
n = int(F.readline())
a = []
for i in range(n):
     s, f = list(map(int, F.readline().split()))
     a.append((s, 1))
     a.append((f+1, -1))
a.sort()
mx = 0
k = 0
for i in range(len(a)):
    k += a[i][1]
    if k > mx:
        mx = k
        cnt = 1
    elif k == mx - 1 and a[i][1] == -1:
        t = a[i][0]  # время окончания пика ?
    elif k == mx and a[i][0] != t: # если по времени разрыв то считаем пик
        cnt += 1    
print(mx, cnt)

