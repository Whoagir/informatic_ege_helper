F = open('26-6.txt')
n, k, m = map(int, F.readline().split())
a = []
for s in F:
    x, y = s.split()
    a.append([int(x), ord(y)])
    
    
#a.sort(reverse = True)
a.sort(reverse = True, key = lambda x: (x[0], -x[1]) )
#print(a[:20])
ans = 0
cntm = 0
for i in range(len(a)-1):
    if a[i][0] == 0:
        continue
    prev = [a[i][0], a[i][1]]
    a[i][0] = 0
    cnt = 1
    for j in range(i + 1, n):
        if a[j][0] != 0 and a[j][0] <= prev[0] - k and a[j][1] != prev[1]:
            cnt += 1
            if cnt == m:
                cntm += 1
                a[j][0] = 0
                break
            prev = [a[j][0], a[j][1]]
            a[j][0] = 0
    ans += 1

print(a[:20])
print(cntm, ans)


