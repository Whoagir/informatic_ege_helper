from functools import cache

@cache
def F( n ):
  return 1 if n == 0 else \
         F(n // 8) * (n % 8) if n % 2 != 0 else \
         F(n // 8)

L = 9
"""
count = 0
for n in range(8**L,8**(L+1)+1):
  count += (F(n) == 25)
print( count )
"""
d = "01246"
k = len(d)
print( len('5')*k**(L-1)*L +
       len('1246')*k**(L-2)*L*(L-1)//2 )
