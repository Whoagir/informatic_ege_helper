import sys
sys.setrecursionlimit( 3100 )
def f( n, x ):
  return n if n >= 3000 else \
         n + 2*x + f(n+2, x)

for x in range(-100, 100):
  if f(28, x) - f(34, x) == 324:
    print(x)
    break
