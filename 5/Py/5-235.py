def alg( x ):
  s = bin(x)[2:]
  for i in range(2):
    if s.count('1') > s.count('0'):
      s += '0'
    else:
      s = '11' + s
  return int(s,2)

N = 1
while True:
  R = alg(N)
  if R > 500:
    print(N, R, bin(R))
    break
  N += 1

