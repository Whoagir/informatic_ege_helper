import sys

sys.setrecursionlimit(10000)

def F( n ):
  return n if n <= 2 else \
         n + F(n-2)

print( F(2023) + F(2020) )

