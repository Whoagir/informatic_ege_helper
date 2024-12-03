import sys
sys.setrecursionlimit( 2000 )
def f( n ):
  return n if n >= 1300 else \
         n*f(n+1) if n % 2 == 1 else \
         n*f(n+2)/4

print( f(1286)/f(1290) )

f = [0] * 1311
for n in range(1310, 0, -1):
    if n >= 1300:
        f[n] = n
    elif n % 2 != 0:
        f[n] = n * f[n + 1]
    else:
        f[n] = n * (f[n + 2])/4

print( f[1286]/f[1290] )