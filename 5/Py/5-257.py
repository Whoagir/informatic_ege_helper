def alg(x):
  s0 = s = "{:b}".format(x)
  if s.count('1') % 2 == 0:
    s += '0'
  else:
    s += '1'
  if s0.count('1') > s0.count('0'):
    s += '0'
  else:
    s += '1'
  return s

for x in range(1,30):
  print(x, int(alg(x),2))