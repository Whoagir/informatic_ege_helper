def mod( n ):
  n = 2*n
  return n % 10 + n // 10

def is_correct( n ):
  s = sEven + sOdd
  isEven = True
  while n:
    s += n % 10 if isEven else mod(n%10)
    n //= 10
    isEven = not isEven
  return s % 10 == 0

sEven = 8 + 6 + 4 + 2
sOdd = mod(7) + mod(5) + mod(3) + mod(1)

n = 9101_1121 + 1
while not is_correct( n ):
    n += 1
print( n )
