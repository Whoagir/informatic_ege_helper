def alg( n ):
  s = f"{n:b}"
  if s.count('1') % 2 == 0:
    s = '10' + s[2:] + '0'
  else:
    s = '11' + s[2:] + '1'
  return int( s, 2 )

for n in range(1000):
  if alg( n ) >= 16:
    break

print( n )

