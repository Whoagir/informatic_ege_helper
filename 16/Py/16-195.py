import sys
sys.setrecursionlimit( 5500 )
def f( n ):
  return n if n >= 5000 else \
         n*f(n+1) if n % 5 > 0 else \
         n*f(n+2)//5

print( f(4975)/f(4978) )
