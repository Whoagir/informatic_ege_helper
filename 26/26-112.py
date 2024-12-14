with open('26-112.txt') as F:
  N, M = map( int, F.readline().split() )
  data = []
  for _ in range(M):
    t0, delta = map(int, F.readline().split())
    data.append( (t0, delta) )

data.sort( key = lambda x: x[0] )

tFree = [0]*N

TMAX = 24*60
i = 0
queue = []
for t in range(TMAX):
  while i < len(data) and data[i][0] <= t:
    queue.append( data[i][1] )
    i += 1
  #print( t, queue )
  while queue:
    delta, placed = queue[0], False
    for k in range(N):
      if tFree[k] <= t:
        tFree[k], kLast = t + delta, k
        placed = True
        #print( '>', k, t, t+delta )
        queue.pop(0)
        break
    if not placed: break

print( M - len(queue), kLast + 1 )
