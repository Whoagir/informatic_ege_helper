from sys import setrecursionlimit
setrecursionlimit( 2500 )
def f( n ):
  if n == 1: return 6
  return 3*n + 2 + f( n-1 )

print( f(2024) - f(2020) )