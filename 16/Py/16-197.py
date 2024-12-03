from functools import cache

@cache
def F( n ):
  return 0 if n == 0 else \
         F(n // 10) + n%10 if n % 2 != 0 else \
         F(n // 10)
"""
count = 0
for n in range(1*10**9,6*10**9+1):
  count += F(n) == 0
print( count )
"""

d = "02468"
k = len(d)
print( len('24')*k**9 + 1 )
