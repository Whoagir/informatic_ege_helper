digits = '0123456789ABCDEF'
def tobase( n, b ):
  if n < b: return digits[n]
  return tobase(n//b, b) + digits[n%b]

def alg( N ):
  s = tobase( N, 3 )
  if N % 2 == 0:
    s = '2' + s + tobase(2*digits.index(s[-1]), 3)
  else:
    s = tobase(2*digits.index(s[0]), 3) + s + '2'
  return int(s, 3)

results = []
for N in range(1000):
  R = alg( N )
  if R > 100:
    results.append( R )

print( min(results) )