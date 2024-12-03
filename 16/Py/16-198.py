from functools import cache

@cache
def F( n ):
  return 0 if n == 0 else \
         F(n // 10) + n%10 if n % 2 == 0 else \
         F(n // 10)

L = 9
"""
count = 0
for n in range(1*10**L,6*10**L+1):
  count += F(n) == 2
print( count )
"""
d = "013579"
k = len(d)
print( len('135')*k**(L-1)*L + len('2')*k**L )
