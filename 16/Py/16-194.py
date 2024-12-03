import sys
sys.setrecursionlimit( 2000 )
def f( n ):
  return n if n >= 1900 else \
         n*f(n+1) if n % 3 > 0 else \
         n*f(n+2)//3

print( f(1875)/f(1880) )
