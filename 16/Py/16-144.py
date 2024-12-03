import sys

sys.setrecursionlimit(20000)

def F( n ):
  return n if n >= 5000 else \
         1 + F(n//2) if n % 2 == 0 else \
         n*n + F(n+2)

print( F(192) - F(9) )