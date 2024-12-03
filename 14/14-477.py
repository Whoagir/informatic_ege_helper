def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

for x in range(7050, 0, -1):
  n = 5 ** 100 - x
  s = toBase( n, 5 )
  if s.count('0') == 3:
    print( x )
    break