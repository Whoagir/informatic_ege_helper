import sys

sys.setrecursionlimit(10000)

def F( n ):
  return 3 if n < 3 else 2*n + 5 + F(n-2)

print( F(3027) - F(3023) )