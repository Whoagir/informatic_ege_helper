
def isPrime( n ):
  return n == 2 or \
         all( n % d != 0 for d in range(2,round(n**0.5)+1) )

def alg( s ):
  while '00' not in s:
    s = s.replace( '02', '101', 1 )
    s = s.replace( '11', '2', 1 )
    s = s.replace( '012', '30', 1 )
    s = s.replace( '010', '00', 1 )
  return s

from random import shuffle

def findStr( s, sumDig = 0 ):
  s = list(s)
  sumDig = sumDig or sum(map(int, s))
  while True:
    sd = sum( map(int, alg('0'+''.join(s)+'0')) )
    if sd == sumDig:
      if isPrime(sumDig):
        print( '0'+''.join(s)+'0' )
        print( alg('0'+''.join(s)+'0') )
        print( s.count('1') )
        print( sum(map(int,alg('0'+''.join(s)+'0'))) )
      return sumDig
    shuffle( s )

n = 61
while True:
  s0 = '1'*n + '2'*80
  sumDig = findStr( s0 )
  if isPrime( sumDig ):
    print( n )
    break
  sumDig = findStr( s0, sumDig-1 )
  if isPrime( sumDig ):
    print( '*', n )
    break
  n += 1