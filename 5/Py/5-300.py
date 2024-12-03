def alg( n ):
  s = f"{n:b}"[1:]
  s = '10' + s if s.count('1') % 2 == 0 else \
      '1' + s + '0'
  return int( s, 2 )

ma = (0, 0)
for n in range(1, 10000):
  R = alg(n)
  if ma[1] < R < 450:
    ma = (n, R)

print( ma )
