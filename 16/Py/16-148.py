import sys

sys.setrecursionlimit(20000)

def F( n ):
  return n if n >= 10000 else \
         F(n + 1) + n**2 - 3*(n-1) if n % 2 == 0 else \
         F(n + 2) + 4*n + 1

print( F(9950) - F(9999) )