def alg( n ):
  s = f"{n:b}"
  if n % 2 == 0:
    s = '10' + s + '1'
  else:
    s = '1' + s + '01'
  return int(s, 2)

for n in range(1000):
  if alg(n) > 420:
    print( n )
    break