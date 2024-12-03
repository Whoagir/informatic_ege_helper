def D( x, d ):
  return x % d == 0
def f( x, A):
  return (x + A >= 160) or (D(x, 7) <= (x - 17 <= 0))

A = 1
while True:
  if all( f(x,A) for x in range(1,1000) ):
    print( A )
    break
  A += 1