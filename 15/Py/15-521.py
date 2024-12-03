def ПОЗ( x, y ):
  return x > y
def f( x, y, A):
  return not ПОЗ(x+y,73) or not ПОЗ(37,x-y) or ПОЗ(y, A)

for A in range(1000):
  if all( f(x,y,A) for x in range(1000) for y in range(1000)):
    print( A )
