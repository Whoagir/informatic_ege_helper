# Автор: К. Багдасарян

from math import gcd
data = [int(x) for x in open('17-411.txt')]
n = len(data)
cnt = 0
mn = float('inf')
for i in range(n-1):
    if (data[i]+data[i+1])%2 != 0 and gcd(data[i],data[i+1]) == 1:
        cnt += 1
        mn = min(mn, data[i]+data[i+1])
print(cnt, mn)
