def alg( N ):
  s = f'{N:b}'
  if N % 2 == 0:
    s += '10'
  else:
    s = '1' + s + '01'
  return int(s, 2)

results = []
for N in range(1,13):
  R = alg(N)
  results.append( R )

print( max(results) )
