import sys

sys.setrecursionlimit(20000)

def F( n ):
  return n if n >= 250 else \
         n//4 + F(n//4 + 2) if n % 4 == 0 else \
         1 + F(n+2)

print( F(174) - F(3) )