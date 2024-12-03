import sys

sys.setrecursionlimit( 2500 )

def f( n ):
  return 1 if n == 1 else 3*n*f(n-1)

print( (f(2024)//6 + f(2023)) / f(2022) )

print( (f(2024) + 6*f(2023)) / (6*f(2022)) )

