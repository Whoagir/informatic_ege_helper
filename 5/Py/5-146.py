def alg( x ):
  s = bin(x)[2:]
  odd = s.count('1') % 2 == 1
  s = s + s[-1]
  if odd:
    s += '1'
  else:
    s += '0'
  odd = s.count('1') % 2 == 1
  if odd:
    s += '1'
  else:
    s += '0'
  return s

MAX = 100000
mi = 10**10
Nmi = 0
for N in range(1, MAX):
  R = int( alg(N), 2 )
  if R > 130 and R < mi:
    mi = R
    Nmi = N

print( mi, Nmi )


