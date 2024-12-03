def f( s ):
  while '00' not in s:
    s = s.replace( '02', '101', 1 )
    s = s.replace( '11', '2', 1 )
    s = s.replace( '12', '21', 1 )
    s = s.replace( '010', '00', 1 )
  return s

def isPrime( n ):
  return n == 2 or \
         all( n % d != 0 for d in range(2,round(n**0.5)+1) )

def isSpec( n ):
  s = str(n)
  return isPrime(n) and s == s[::-1]

for n in range(100, 300):
  s = '0' + n*'1' + n*'2' + '0'
  s1 = f(s)
  sumDig = sum( map(int, s1) )
  if isSpec(sumDig):
    print( n, sumDig )
    break
