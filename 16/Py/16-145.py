import sys

sys.setrecursionlimit(20000)

def F( n ):
  return n if n >= 2000 else \
         n//6 + F(n//6 + 2) if n % 6 == 0 else \
         n + F(n+2)

print( F(264) - F(7) )