def fromBase( x, base ):
  n = 0
  for c in x:
    n = base*n + c
  return n

D = 4221
for x in range(95):
  for y in range(95):
    n = fromBase( [1, x, y, x, 5], 95 ) + fromBase( [6, y, x, 1, 7], 95 )
    if n % D == 0:
      print( x, y, hex(n // D)[2:] )