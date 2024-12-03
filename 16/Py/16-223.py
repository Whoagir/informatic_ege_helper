import sys

sys.setrecursionlimit( 2500 )

def F( n ):
  return 1 if n <= 2025 else F((n+2024)//2025) + 1

print( F( sum(i**i for i in range(1,2026)) ) )

