from functools import lru_cache
import sys

sys.setrecursionlimit( 10000 )

@lru_cache
def F( n ):
  return 1 if n < 4 or n % 2 == 1 else \
         F(n-1) + F(n-2) + F(n-3)

print( F(2008) - F(2006) )