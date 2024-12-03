def baseToDec( coeff, base ):
  s = 0
  for i in range(len(coeff)):
    s += coeff[-1-i]*base**i
  return s

for x in range(1,45):
  n1 = baseToDec( [1, x, 0, 6, 1], 45 )
  n2 = baseToDec( [x, 2, 0, 2, 4], 45 )
  n3 = baseToDec( [1, x, 17, 7], 45 )
  n = n1 + n2 - n3
  if n % 44 == 0:
    print( x, n )
