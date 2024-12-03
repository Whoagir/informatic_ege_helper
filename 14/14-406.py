import string

A = string.digits + string.ascii_uppercase

def fromBase( s, base, x ):
  n = 0
  for c in s:
    if c in A:
          n = base*n + A.index(c)
    else: n = base*n + x
  return n

D = 111
for x in range(0,111):
  n = fromBase( 'x321', 111, x ) + fromBase( '17x4', 211, x )
  if n % D == 0:
    print( x, n // D )