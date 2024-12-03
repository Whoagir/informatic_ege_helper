def isPrime( n ):
  return n == 2 or \
         all( n % d != 0 for d in range(2,round(n**0.5)+1) )

def alg( s ):
  while '91' in s or '92' in s:
    if '91' in s:
      s = s.replace( '91', '39', 1 )
    if '92' in s:
      s = s.replace( '92', '59', 1 )
  return s

n = 1
while True:
  s = alg( '9' + n*'1' + n*'2' )
  sumDigits = sum( map(int, s) )
  if 100 <= sumDigits <= 999 and isPrime( sumDigits ):
    print( n )
    break
  n += 1
