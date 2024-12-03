digits = '0123456789ABCDEF'
def tobase( n, b ):
  if n < b: return digits[n]
  return tobase(n//b, b) + digits[n%b]

def alg( N ):
  s = tobase( N, 13 )
  for i in range(2):
    sumDigits = sum( digits.index(c) for c in s )
    s += tobase( sumDigits % 13, 13 )
  return int(s, 13)

results = []
for N in range(1000):
  R = alg( N )
  if R < 6000:
    results.append( (R, N) )

print( sorted(results, reverse = True)[0] )