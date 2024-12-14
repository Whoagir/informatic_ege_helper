with open( '26-90.txt' ) as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

data.sort()

S = sum(data)
D = 4
Nact = N // D

print( S - sum(data[-Nact:])//2, S - sum(data[:Nact])//2 )
