with open('26-141a.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    t0, t1 = map( int, F.readline().split() )
    data.append( (t0, t1) )

data.sort( key = lambda p: p[1] )

count = 0
tFree = 0
for tStart, tEnd in data:
  if tStart >= tFree:
    count += 1
    tFree = tEnd

print( count, data[0][1] )
