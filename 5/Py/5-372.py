def alg( N ):
  s = f'{N:b}'
  if s.count('1') % 2 == 0:
    s = '10' + s[2:] + '0'
  else:
    s = '11' + s[2:] + '1'
  return int(s, 2)

for N in range(1000):
  R = alg( N )
  if R > 50:
    print( N )
    break
