def tobase( n, b ):
  if n < b: return str(n)
  return tobase(n//b, b) + str(n%b)
def alg( N ):
  s = tobase( N, 4 )
  if N % 4 == 0:
    s += s[-2:]
  else:
    s += tobase( (N%4)*5, 4 )
  return int(s, 4)

for N in range(100):
  R = alg( N )
  if R < 555:
    print( N )