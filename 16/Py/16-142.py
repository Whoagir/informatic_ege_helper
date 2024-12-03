from functools import lru_cache
import sys

sys.setrecursionlimit( 10000 )

@lru_cache
def F( n ):
  q = n**0.5
  return round(q) if q % 1 == 0 else \
         F(n+1) + 1

print( F(4850) + F(5000)  )