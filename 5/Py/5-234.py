def alg( x ):
  s = bin(x)[2:]
  if s.count('1') > s.count('0'):
    s += '0'
  else:
    s += '1'
  m = len(s) // 2
  if len(s) % 2 == 0:
    s = s[:m-1] + s[m+1:]
  else:
    s = s[:m-1] + s[m+2:]
  return s

MAX = 100000
d = {}
for N in range(10, MAX):
  R = int( alg(N), 2 )
  #print( N, R )
  d[R] = 1

count = 0
for R in range(50, 100):
  if R in d:
    print(R)
    count += 1

print( count )
