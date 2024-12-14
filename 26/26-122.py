with open('26-122.txt') as F:
  K, N = map( int, F.readline().split() )
  data = []
  for _ in range(N):
    t0, tEnd = map( int, F.readline().split() )
    data.append( (t0, tEnd) )

data.sort()

lastLine = 0
freeTime = [0]*(N+1)
for t0, tEnd in data:
  freeTime = [ 0 if t < t0 else t for t in freeTime ]
  pos = freeTime.index( 0 )
  freeTime[pos] = tEnd
  lastLine = max( pos // K, lastLine )

print( lastLine + 1, (N+1) - freeTime.count(0) )

