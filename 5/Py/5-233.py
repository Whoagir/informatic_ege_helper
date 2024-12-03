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

count = 0
MAX = 100000
for N in range(10, MAX):
  R = alg(N)
  #print(N, int(R,2))
  if int(R, 2) == 58:
    print( N )
    count += 1
    #break

print( count )

