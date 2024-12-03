def isPalindrome( n ):
  s = str(n)
  return s == s[::-1]

def alg( s ):
  while '01' in s or '02' in s:
    s = s.replace('02', '1110', 1)
    s = s.replace('01', '220', 1)
  return s

results = []
for n in range(55, 200):
  for k1 in range(1, n):
    k2 = n - 1 - k1
    if isPalindrome(4*k1 + 3*k2):
      s = '0' + k1*'1' + k2*'2'
      r = alg( s )
      sumDigits = sum( map(int, r) )
      results.append( (k1+2*k2, 4*k1 + 3*k2, sumDigits) )

print( min(results) )