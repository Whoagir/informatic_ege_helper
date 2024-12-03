def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

for x in range(3000, 0, -1):
  n = 7 ** 100 - x
  s = toBase( n, 7 )
  if s.count('0') == 2:
    print( x )
    break