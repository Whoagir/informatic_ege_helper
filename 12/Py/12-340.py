
def alg( s ):
  while '>1' in s or '>2' in s or '>0' in s:
    if '>1' in s:
      s = s.replace( '>1', '22>', 1 )
    if '>2' in s:
      s = s.replace( '>2', '2>', 1 )
    if '>0' in s:
      s = s.replace( '>0', '1>', 1 )
  return s

def isPrime( n ):
  return n == 2 or \
         all( n % d != 0 for d in range(2,n) )

for n in range(10, 100):
  if isPrime(n):
    s = '>' + 21*'0' + n*'1' + 11*'2'
    sd = sum( map(int, alg(s)[:-1]) )
    if sd % n == 0:
      print( n )

