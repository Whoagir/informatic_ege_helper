import sys

sys.setrecursionlimit(20000)

def F( n ):
  return n if n >= 10000 else \
         n + F(n//3) if n % 3 == 0 else \
         2*n + F(n+3)

print( F(999) - F(46) )