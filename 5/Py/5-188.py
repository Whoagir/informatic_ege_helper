def alg( x ):
  s = "{:08b}".format(x)
  s1 = ""
  doInversion = False
  for c in reversed(s):
    if not doInversion:
      if c == '1': doInversion = True
      s1 = c + s1
    else:
      if c == '1': s1 = '0' + s1
      else:        s1 = '1' + s1
  return int(s1,2)

for i in range(1, 256):
  print( i, alg(i) )
  if alg(i) == 171:
    break
