from functools import lru_cache
import sys

sys.setrecursionlimit( 5000 )

@lru_cache
def F( n ):
  return 1 if n < 4 else \
         n if n % 2 == 1 else \
         F(n-1) + F(n-2) + F(n-3)

print( F(2254) - F(2252) )