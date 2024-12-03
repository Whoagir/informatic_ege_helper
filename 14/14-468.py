def val( x, b ):
  n = 0
  for xi in x:
    n = n*b + xi
  return n

def isSquare( x ):
  q = round(x**0.5)
  return q*q == x

b = 57
results = []
for x in range(b):
  for y in range(b):
    n = val( [5,3,x,6,6,y,3,5], b )
    if n % (b-1) == 0:
      results.append( (x, y) )

ma = [ x for x in results
         if isSquare( x[1]*b+x[0] )  ]

ma.sort( key = lambda x: x[1]*b+x[0] )
print( ma )
ma = ma[-1]

print( ma, ma[1]*b + ma[0] )

print( ma[0]*b + ma[1] )