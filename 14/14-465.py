def val( x, b ):
  n = 0
  for xi in x:
    n = n*b + xi
  return n

b = 63
results = []
for x in range(b):
  for y in range(b):
    n = val( [3,x,4,x,y,5,6,y], b )
    if n % (b-1) == 0:
      results.append( (x, y) )

ma = max( results, key = lambda x: x[0]*b+x[1] )

print( ma )
print( ma[0]*b*b + ma[1]*b + ma[0] )