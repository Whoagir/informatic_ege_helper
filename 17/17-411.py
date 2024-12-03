# Автор: К. Багдасарян

from math import gcd
data = [int(x) for x in open('17-411.txt')]
n = len(data)
cnt = 0
mn = min(data)%10
mx = -float('inf')
for i in range(n-1):
    if gcd(data[i], data[i+1]) % 10 == mn:
        cnt += 1
        mx = max(mx, data[i]+data[i+1])
print(cnt, mx)


