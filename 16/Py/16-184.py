import sys

sys.setrecursionlimit(10000)

def F( n ):
  return n if n < 11 else n + F(n-1)

print( F(2024) - F(2021) )