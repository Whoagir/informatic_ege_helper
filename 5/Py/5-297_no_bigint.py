def mod( n ):
  n = 2*n
  return n % 10 + n // 10

def control_sum( n ):
  s = sEven + sOdd
  isEven = True
  while n:
    s += n % 10 if isEven else mod(n%10)
    n //= 10
    isEven = not isEven
  return s

sEven = 0 + 0 + 0 + 0
sOdd = mod(0) + mod(0) + mod(0) + mod(1)

num = 0
while control_sum(num) != 30:
    num += 1
print( num )
