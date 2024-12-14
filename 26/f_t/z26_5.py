F = open('26-5.txt')
n, k = map(int, F.readline().split())
a = []
for s in F:
    x, y = s.split()
    a.append([int(x), y])
    
    
a.sort(reverse = True)
#print(a[:20])
mx = 0
ans = 0
for i in range(len(a)-1):
    if a[i][0] == 0:
        continue
    prev = [a[i][0], a[i][1]]
    a[i][0] = 0
    cnt = 1
    for j in range(i + 1, n):
        if a[j][0] != 0 and a[j][0] <= prev[0] - k and a[j][1] != prev[1]:
            cnt += 1
            prev = [a[j][0], a[j][1]]
            a[j][0] = 0
    ans += 1
    if cnt > mx:
        mx = cnt
        
#print(a[:20])
print(mx, ans)


