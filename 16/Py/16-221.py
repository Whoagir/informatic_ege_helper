import sys

sys.setrecursionlimit( 2500 )

def F( n ):
  return 1 if n < 3 else F((n+1)//2) + 1

print( F( sum( 2**i for i in range(1,2026) ) ) )

