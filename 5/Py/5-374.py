def alg( N ):
  s = f'{N:b}'
  if N % 2 == 0:
    s = '10' + s
  else:
    s = '1' + s + '01'
  return int(s, 2)

results = []
for N in range(12,0,-1):
  results.append( alg( N ) )

print( max(results) )
