import sys

sys.setrecursionlimit( 2500 )

def F( n ):
  return 1 if n < 3 else F((n+1)//2) + 1


print( F(2**2025) )

