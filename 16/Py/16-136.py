from functools import lru_cache
import sys

sys.setrecursionlimit( 5000 )

@lru_cache
def F( n ):
  return 1 if n < 3 else \
         F(n-1) + F(n-2)

print( (F(1006) - F(1004)) // F(1005) )