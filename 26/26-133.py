with open('26-123.txt') as F:
  M, N = map( int, F.readline().split() )
  data = []
  for _ in range(N):
    tStart, dt, pStart, pEnd = map(int, F.readline().split())
    data.append( (tStart, tStart+dt, pStart-1, pEnd-1) )

data.sort()

free = [ [] for _ in range(M) ]

maxCount = [0]*M
maxActive = 0
tMaxActive = 0
for tStart, tEnd, pStart, pEnd in data:
  for t in free[pStart]:
    if tStart >= t:
      free[pStart].remove( t )
      break
  else:
    maxCount[pStart] += 1
  free[pEnd].append( tEnd )
  activeNow = sum( len( [t for t in f if t > tStart] )
                for f in free )
  if activeNow > maxActive:
    tMaxActive = tStart
    maxActive = activeNow

print( tMaxActive, maxCount.index(max(maxCount))+1 )
