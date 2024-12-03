def alg( n ):
  s = f"{n:b}"
  s += '100' if s.count('1') % 4 == 0 else '110'
  return int(s, 2)

for n in range(1, 100):
  R = alg(n)
  if R < 250:
    nMax = n

print( nMax )
