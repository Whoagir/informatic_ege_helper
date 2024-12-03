def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

for x in range(8300, 10000):
  n = 5 ** 100 - x
  s = toBase( n, 5 )
  if s.count('0') == 4:
    print( x )
    break