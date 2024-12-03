def baseToDec( coeff, base ):
  s = 0
  for i in range(len(coeff)):
    s += coeff[-1-i]*base**i
  return s

for x in range(1,47):
  n1 = baseToDec( [1, x, 2, 4, 10], 47 )
  n2 = baseToDec( [x, 2, 0, 2, 4], 47 )
  n3 = baseToDec( [6, x, 0, 8], 47 )
  n = n1 + n2 - n3
  if n % 46 == 0:
    print( x, n )
