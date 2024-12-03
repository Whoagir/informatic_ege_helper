import sys

sys.setrecursionlimit(20000)

def F( n ):
  return n if n >= 10000 else \
         F(n + 2) - 3 if n % 2 == 0 else \
         F(n + 2) + 1

print( F(9994)-F(9980) )