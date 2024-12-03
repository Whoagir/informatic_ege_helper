import sys

sys.setrecursionlimit(3100)

def F( n ):
  return 7 if n < 7 else \
         5 - F(n - 1) if n % 3 != 0 else \
         3 + F(n - 1)

print( F(3015) )
