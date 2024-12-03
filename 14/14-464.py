def val( x, b ):
  n = 0
  for xi in x:
    n = n*b + xi
  return n

b = 57
results = []
for x in range(b):
  for y in range(b):
    n = val( [5,x,2,7,y,3,2,y], b )
    if n % (b-1) == 0:
      results.append( (x, y) )

ma = max( results, key = lambda x: x[0]*b+x[1] )

print( ma )
print( ma[0]*b+ma[1] )