def alg( x ):
  s = "{:b}".format(x)
  if s.count('1') > s.count('0'):
    s += '1'
  else:
    s += '0'
  return int(s, 2)

for i in range(1, 100):
  print( i, alg(i) )
  if alg(i) > 100:
    break
