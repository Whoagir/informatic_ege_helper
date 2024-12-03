from math import gcd
data = [int(x) for x in open('1.txt')]
n = len(data)
cnt = [0]*1001
sm = [0]*1001
for i in range(n-1):
    j = gcd(data[i], data[i+1])
    cnt[j] += 1
    sm[j] = max(sm[j], data[i]+data[i+1])
i = cnt.index(max(cnt))
print(i, sm[i])
