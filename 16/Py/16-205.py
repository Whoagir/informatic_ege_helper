from functools import cache

@cache
def F( n ):
  return 1 if n == 0 else \
         F(n // 10) * (n % 10) if n % 2 != 0 else \
         F(n // 10)

L = 9
"""
count = 0
for n in range(10**L,10**(L+1)+1):
  count += (F(n) == 49)
print( count )
"""
d = "012468"
k = len(d)
print( len('7')*k**(L-1)*L +
       len('12468')*k**(L-2)*L*(L-1)//2 )
