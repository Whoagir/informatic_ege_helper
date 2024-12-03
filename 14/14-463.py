def val( x, b ):
  n = 0
  for xi in x:
    n = n*b + xi
  return n

b = 39
results = []
for x in range(b):
  for y in range(b):
    n = val( [1, 2, x, 4, 5, 6, y, 8], b )
    if n % 38 == 0:
      results.append( (x, y) )

ma = max( results, key = lambda x: x[0]*b+x[1] )

print( ma )
print( ma[0]*b+ma[1] )