from functools import cache

@cache
def F( n ):
  return 1 if n == 0 else \
         F(n // 10) * (n % 10) if n % 2 != 0 else \
         F(n // 10)

L = 9
"""
count = 0
for n in range(10**L,6*10**L+1):
  count += (F(n) == 15)
print( count )
"""

d = "012468"
k = len(d)
print( len('3')*k**(L-1)*L + len('5')*k**(L-1)*L +
       len('124')*k**(L-2)*L*(L-1) )
