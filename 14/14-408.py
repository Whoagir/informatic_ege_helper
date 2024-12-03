def fromBase( x, base ):
  n = 0
  for c in x:
    n = base*n + c
  return n

digits = '0123456789ABCDEF'
def toBase( n, base ):
  s = ''
  while n:
    s = digits[n%base] + s
    n //= base
  return s

maxZeros = 0
for x in range(32):
  n = fromBase( [1, 7, 9, x, 9], 32 ) + \
      fromBase( [7, x, 9, 3], 128 )
  z = toBase(n, 4).count('0')
  if z > maxZeros:
    maxZeros = z
    print( x, z, toBase(n, 4),
           sum( map(int, toBase(n, 4)) ) )