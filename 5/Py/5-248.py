def alg( x ):
  s = bin(x)[2:]
  for i in range(3):
    if s.count('0') == s.count('1'):
      s += s[-1]
    elif s.count('0') < s.count('1'):
      s += '0'
    else:
      s += '1'
  return int(s, 2)

MAX = 10000
for N in range(100+1, MAX):
  R = alg(N)
  if R % 2 == 0 and R % 4 != 0:
    print( N, R )
    break

