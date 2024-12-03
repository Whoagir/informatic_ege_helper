def ДЕЛ( x, d ): return x % d == 0
def f( x, A):
  return (ДЕЛ(x, 2) <= (not ДЕЛ(x, 13))) or  (x + A >= 1000)

for A in range(1,1000):
  if all( f(x,A) for x in range(1,1000)):
    print( A )
    break
