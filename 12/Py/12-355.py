def isPrime( n ):
  return n > 1 and \
         all( n % d != 0 for d in range(2,round(n**0.5)+1))

def alg( s ):
  while '01' in s or '02' in s:
    s = s.replace('02', '1110', 1)
    s = s.replace('01', '2210', 1)
  return s

results = []
for n in range(95, 100):
  for k1 in range(1, n):
    k2 = n - 1 - k1
    if isPrime(5*k1 + 3*k2):
      s = '0' + k1*'1' + k2*'2'
      r = alg( s )
      sumDigits = sum( map(int, r) )
      results.append( (k1+2*k2, 5*k1 + 3*k2, sumDigits) )

print( min(results) )