def alg( N ):
  sN = bin(N)[2:]
  sR = sN + sN[-2] + sN[1]
  R = int( sR, 2 )
  return R

TARGET = 165

N = 2
while alg(N+1) <= TARGET:
  N += 1
print( N )


