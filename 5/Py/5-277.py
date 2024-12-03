def alg(x):
  digits = list(map(int, str(x)))
  s1 = sum( d for d in digits if d % 2 != 0 )
  s2 = sum( digits[1::2] )
  return abs(s1-s2)


N = 1
while True:
  if alg(N) == 30:
    print(N)
    break
  N += 1
