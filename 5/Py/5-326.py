def alg( n ):
  s = f"{n:b}"
  if n % 2 == 0:
    s = '1' + s + str(s.count('1')%2)
  else:
    s = s + '0' + str(s.count('1')%2)
  return int(s, 2)

minR = 10**10
for n in range(1, 100):
  R = alg(n)
  if R > 100:
    if R < minR:
      nMin, minR = n, R

print( nMin )
