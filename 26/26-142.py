with open('26-142.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    t0, t1 = map( int, F.readline().split() )
    data.append( (t0, t1) )

data.sort( key = lambda t: t[1] )

delta = 10
count = 1
tPrev = - delta
tFree = data[0][1] + delta
print( *data[0] )
for t0, t1 in data[1:]:
  if t0 >= tFree:
    count += 1
    print( t0, t1 )
    tPrev = tFree - delta
    tFree = t1 + delta

candidates = [ d[0] for d in data if d[1] >= tPrev+delta ]
maxSpan = max(candidates) - tPrev

print( count, maxSpan )