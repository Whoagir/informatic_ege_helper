import sys

sys.setrecursionlimit( 2500 )

def f( n ):
  return 1 if n == 1 else (n+1)*f(n-1)


print( (f(2024) - 3*f(2023)) / f(2022) )

