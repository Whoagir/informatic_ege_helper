import sys

sys.setrecursionlimit(10000)

def F( n ):
  return 1 if n == 1 else \
         n + F(n-1)

print( F(2023) - F(2019) )

