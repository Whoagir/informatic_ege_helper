x = 1
for n in range(1000, 997, -1):
  x *= n

print( x - 1 )

from functools import lru_cache
import sys

sys.setrecursionlimit( 10000 )

@lru_cache
def f( n ):
  return 1 if n == 1 else \
         n*f(n-1) - 1

print( f(1000) // f(997) )