import sys

sys.setrecursionlimit(10000)

def F( n ):
  return n if n >= 2022 else 7 + F(n+5)

print( F(45) - F(49) )