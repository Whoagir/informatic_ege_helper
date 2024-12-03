def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

for x in range(1,2030):
  n = 6**260 + 6**160 + 6**60 - x
  s = toBase( n, 6 )
  if s.count('0') == 202:
    print( x )
    break