def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

for x in range(5000, 100000):
  n = 7 ** 100 - x
  s = toBase( n, 7 )
  if s.count('0') == 5:
    print( x )
    break