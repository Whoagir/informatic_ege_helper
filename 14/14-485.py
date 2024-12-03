def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

for x in range(2030, 0, -1):
  n = 7 ** 170 + 7**100 - x
  s = toBase( n, 7 )
  if s.count('0') == 71:
    print( x )
    break