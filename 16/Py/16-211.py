import sys
from functools import cache

sys.setrecursionlimit(5000)

@cache
def F( n ):
  return 2 if n > 2024 else \
         1 if n == 2024 else \
         (n*(n + 1) + F(n + 1) - F(n + 2))

print( F(100) - F(10) + F(2020) )
