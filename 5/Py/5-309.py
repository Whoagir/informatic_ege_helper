def alg( n ):
  s = ''
  for d in str(n):
    sd = f'{int(d):04b}'
    s += sd + '0' if sd.count('1') % 2 == 0 else \
         sd + '1'
  s = '1' + s[2:] + '0'
  return int( s, 2 )

for n in range(1, 10000):
  if alg(n) == 674890:
    print( n )
    break
