def tobase( n, b ):
  if n < b: return str(n)
  return tobase(n//b, b) + str(n%b)
def alg( N ):
  s = tobase( N, 8 )
  if sum(map(int, s)) %2 == 0:
    s = s[0] + s + s[0]
  else:
    s += s[-1]
  return int(s, 8)

for N in range(1000):
  R = alg( N )
  if R < 1100:
    print( N )