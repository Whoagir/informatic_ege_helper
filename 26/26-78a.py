with open('26-78.txt') as F:
  N, tStart, tFinish = [int(x) for x in F.readline().split()]
  periods = []
  for i in range(N):
    t0, t1 = [int(x) for x in F.readline().split()]
    periods.append( (t0, t1) )

periods.sort()

count = 0
i, t = 0, tStart
while t < tFinish:

  while not (periods[i][0] <= t and periods[i][1] > t):
    i += 1

  maxStop = periods[i][1]
  while periods[i][0] <= t:
    maxStop = max( maxStop, periods[i][1] )
    i += 1

  if count == 0:
    tFirst = maxStop - tStart
  count += 1
  t = maxStop

print( count, tFirst )
