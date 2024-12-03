
Kmax = 0
for N in range(1000, 10000):
  s = str(N)
  K = int( "".join( sorted(s, reverse=True) ) )
  M = int( "".join( sorted(s) ) )
  if K - M == 6174 and K > Kmax:
    Kmax = K
    print( N, K )
