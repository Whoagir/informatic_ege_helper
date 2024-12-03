def alg( n, m ):
  pEven = pOdd = 1
  while n:
    digit = n % 10
    if digit % 2 == 1:
      pOdd *= digit
    elif digit:
      pEven *= digit
    n //= 10
  while m:
    digit = m % 10
    if digit % 2 == 1:
      pOdd *= digit
    elif digit:
      pEven *= digit
    m //= 10
  return abs(pEven - pOdd)

N = 120
for M in range(1,1000):
  if alg( N, M ) == 29:
    print( M )
    break


