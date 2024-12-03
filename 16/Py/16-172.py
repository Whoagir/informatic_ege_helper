from math import ceil

a, b = 100000000, 200000000

from math import gcd
count = 0
for i in range(a, b+1):
  if gcd(i, 15) == 3:
    count += 1

print( count )
