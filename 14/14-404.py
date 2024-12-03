import string

A = string.digits + string.ascii_uppercase

def fromBase( s, base, x ):
  n = 0
  for c in s:
    if c in A:
          n = base*n + A.index(c)
    else: n = base*n + x
  return n

for x in range(0,98):
  n = fromBase( '12x45', 98, x ) + fromBase( '1x98', 123, x )
  if n % 123 == 0:
    print( x, n // 123 )