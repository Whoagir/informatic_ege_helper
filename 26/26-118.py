with open('26-118.txt') as F:
  t, N, M = map(int, F.readline().split())
  data = {}
  for id in range(N):
    tStart, tEnd, disCount = map(int, F.readline().split())
    data[id] = [tStart, tEnd, disCount]

count = {}
for t in range(t, 1440, t):
  inside = [ [id]+x for id, x in data.items()
                    if x[0] <= t <= x[1] and x[2] < M ]
  inside.sort( key = lambda x: (x[3], -x[2]) )
  if inside:
    id, tStart, tEnd, disCount = inside[0]
    count[id] = count.get(id, 0) + 1
    data[id][2] += 1

maxItem = max( count.items(), key = lambda x: x[1] )
id, maxCount = maxItem
spentTime = data[id][1] - data[id][0] + 1

print( spentTime, maxCount )

