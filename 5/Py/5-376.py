def alg( N ):
  s = f'{N:b}'
  s += str( s.count('1') % 2 )
  s += str( s.count('1') % 2 )
  return int(s, 2)

results = []
for N in range(1,100):
  R = alg(N)
  if R > 123:
    results.append( R )

print( min(results) )
