with open('26-144.txt') as F:
  N, K = map( int, F.readline().split() )
  data = []
  for i in range(N):
    t0, dt, no = map( int, F.readline().split() )
    data.append( (t0, dt, no-1) )

data.sort()

queue = [ [0]*1441 for i in range(K) ]
freeFrom = [0]*K
count = [0]*K
countFail = 0
for t0, dt, no in data:
  if no < 0:
    queueLength = [ queue[i][t0] for i in range(K)]
    no = queueLength.index( min(queueLength) )
  if queue[no][t0] >= 5:
    countFail += 1
  else:
    count[no] += 1
    tEnd = max(t0, freeFrom[no]) + dt
    for t in range(t0, tEnd):
      if t <= 1440: queue[no][t] += 1
    freeFrom[no] = tEnd

print( count, countFail )