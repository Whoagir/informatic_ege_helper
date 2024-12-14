with open('26-115.txt') as F:
  N, M = map( int, F.readline().split() )
  data = []
  for _ in range(M):
    t0, tEnd = map(int, F.readline().split())
    data.append( (t0, tEnd) )

data.sort( key = lambda x: x[0] )

tFree = [0]*N

TMIN = 10*60
TMAX = 20*60
count, kLast = 0, 0
for t0, tEnd in data:
  if not (TMIN <= t0 and tEnd <= TMAX): continue
  for k in range(N):
    if t0 >= tFree[k]:
      tFree[k] = tEnd + 1
      #print( k, t0, tEnd, tFree )
      count += 1
      kLast = k
      break

print( count, kLast+1 )
