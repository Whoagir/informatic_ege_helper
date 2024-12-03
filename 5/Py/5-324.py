def alg( n ):
  s = f"{n:b}"
  for i in range(2):
    if n % 2 == 1 and s.count('1') % 2 == 1:
      s = '1' + s
    else:
      s += str( s.count('1') % 2 )
  return int( s, 2 )

maxN = 0
for n in range(1,100):
  if alg( n ) < 100:
    maxN = max( n, maxN )

print( maxN )