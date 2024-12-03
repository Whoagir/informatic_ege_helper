def alg( n ):
  s = f"{n:b}"
  if s.count('1') % 2 == 0:
     s = '1' + s + '00'
  else:
     s = '11' + s
  return int(s,2)

i = 1
while True:
  print( i, alg(i) )
  if alg( i ) >= 412:
    print( i )
    break
  i += 1