from functools import cache

@cache
def F( n ):
  return 1 if n == 0 else \
         F(n // 100) * (n % 10) if n % 2 != 0 else \
         F(n // 100)

L = 9
"""
count = 0
for n in range(10**L,6*10**L+1):
  count += (F(n) == 21)
print( count )
"""
d = "012468"
k = len(d)
pFree = (L + 1) // 2
p = L + 1 - pFree
print( len('12345') * 10**(pFree-1) * k**(p-2) * p*(p-1) )
