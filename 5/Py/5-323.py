def alg( n ):
  s = f"{n:b}"
  s += '111' if n % 6 == 0 else '1'
  n = int( s, 2 )
  s += '101' if n % 3 == 0 else '1'
  return int( s, 2 )

for n in range(1,1000000):
  if alg( n ) > 300000:
    print( n )
    break

