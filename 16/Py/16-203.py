from functools import cache

@cache
def F( n ):
  return 0 if n == 0 else \
         F(n // 8) + n%8 if n % 2 != 0 else \
         F(n // 8)

L = 9
"""
count = 0
for n in range(1*8**L,8**(L+1)+1):
  count += F(n) == 1
print( count )
"""
d = "0246"
k = len(d)
print( len('246')*k**(L-1)*L + len('1')*k**L + 1 )
