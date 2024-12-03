def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

from string import digits, ascii_uppercase
let = digits + ascii_uppercase
def toBase( n, b ):
  s = ''
  while n:
    s = let[n%b] + s
    n //= b
  return s

for p in range(9,30):
  for x in range(p):
    for y in range(p):
      for z in range(p):
        n = f( [y, 3, y], p ) + f( [y, 6, 5], p ) - f( [x, 2, z, 0], p )
        if n == 0:
          print( x, y, z, f( [x, y, z], p ) )