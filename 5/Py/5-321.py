def alg( n ):
  s = f"{n:b}"
  s += '11' if n % 3 == 0 else '1'
  n = int( s, 2 )
  s += '101' if n % 5 == 0 else '1'
  return int( s, 2 )

for n in range(1,1000000):
  if alg( n ) < 1000000:
    print( n )

