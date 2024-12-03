# Автор: К. Багдасарян

from math import gcd
data = [int(x) for x in open('17-411.txt')]
n = len(data)
mn = min(x for x in data if x % 10 == 3)
cnt = 0
mx = -float('inf')
for i in range(n-1):
    if mn % gcd(data[i], data[i+1]) == 0:
        cnt += 1
        mx = max(mx, data[i]+data[i+1])
print(cnt, mx)
