with open('26-143.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    t0, dt, no = map( int, F.readline().split() )
    data.append( (t0, dt, no-1) )

data.sort()

LIMIT = 5

queue = [ [0]*1441, [0]*1441 ]
freeFrom = [0, 0]
count = [0, 0]
countFail = 0
for t0, dt, no in data:
  #print( '*', t0, dt, no )
  if no < 0:
    no = 0 if queue[0][t0] <= queue[1][t0] else 1
    #print( no, queue[0][t0], queue[1][t0] )
  if queue[no][t0] >= LIMIT:
    countFail += 1
    #print('x')
  else:
    count[no] += 1
    tEnd = max(t0, freeFrom[no]) + dt
    for t in range(t0, tEnd):
      if t <= 1440: queue[no][t] += 1
    freeFrom[no] = tEnd
  #print( queue[0][10:25] )
  #print( queue[1][10:25] )

print( count, countFail )