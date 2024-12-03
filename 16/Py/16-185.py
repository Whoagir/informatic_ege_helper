import sys

sys.setrecursionlimit(10000)

def F( n ):
  return 7 if n < 7 else n + 1 + F(n-2)

print( F(2024) - F(2020) )