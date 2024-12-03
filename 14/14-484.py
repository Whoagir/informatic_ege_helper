def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

max0 = 0
for x in range(1,2030):
  n = 6**2030 + 6**100 - x
  s = toBase( n, 6 )
  zeros = s.count('0')
  if zeros > max0:
    print( x, zeros )
  max0 = max( zeros, max0 )


print( max0 )
