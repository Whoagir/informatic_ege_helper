from functools import cache

@cache
def F( n ):
  return 0 if n == 0 else \
         F(n // 10) + n%10 if n % 2 != 0 else \
         F(n // 10)

L = 9
"""
count = 0
for n in range(1*10**L,6*10**L+1):
  count += F(n) == 1
print( count )
"""
d = "02468"
k = len(d)
print( len('24')*k**(L-1)*L + len('1')*k**L )
