import sys

sys.setrecursionlimit( 2500 )

def f( n ):
  return 1 if n == 1 else n*f(n-1)

print( (2*f(2024) + f(2023)) / f(2022) )