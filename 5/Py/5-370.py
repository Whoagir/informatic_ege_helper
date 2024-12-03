digits = '0123456789ABCDEF'
def tobase( n, b ):
  if n < b: return digits[n]
  return tobase(n//b, b) + digits[n%b]

def alg( N ):
  s = tobase( N, 12 )
  if N % 12 == 0:
    s += s[-3:]
  else:
    s = tobase((N % 12)*3, 12) + s
  return int(s, 12)

results = []
for N in range(144, 1000):
  R = alg( N )
  if R < 58000:
    results.append( (R, N) )

print( sorted(results, reverse = True)[0] )