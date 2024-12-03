def alg( x ):
  s = ""
  while x:
    s = "{:04b}".format(x%10) + s
    x //= 10
  si = ""
  for c in s:
    if c == '0':
      si += '1'
    else:
      si += '0'
  return si

MAX = 100000
for N in range(1, MAX):
  R = int( alg(N), 2 )
  if R == 151:
    print( N, R )
    break

