def alg2(i):
   n = bin(i)
   n = n[2:]
   n = n + n[-2]
   n = n + n[1]
   n = int(n, 2)
   return n

def alg( N ):
  sN = bin(N)[2:]
  sR = sN + sN[-2] + sN[1]
  R = int( sR, 2 )
  return R

MIN = 150
MAX = 250

N = 2
count = 0
for N in range(2, 1000):
  R = alg(N)
  if MIN <= alg(N) <= MAX:
    count += 1

print( count )


