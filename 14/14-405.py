import string

A = string.digits + string.ascii_uppercase

def fromBase( s, base, x ):
  n = 0
  for c in s:
    if c in A:
          n = base*n + A.index(c)
    else: n = base*n + x
  return n

D = 567
for x in range(0,109):
  n = fromBase( 'x751', 109, x ) + fromBase( '237x', 215, x )
  if n % D == 0:
    print( x, n // D )