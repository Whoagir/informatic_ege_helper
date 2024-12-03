from functools import lru_cache
import sys

sys.setrecursionlimit( 5000 )

@lru_cache
def F( n ):
  return 2 if n == 1 else \
         2*F(n-1)

print( F(1900) // 2**1890 )


# Вариант 2

print( 2**10 )