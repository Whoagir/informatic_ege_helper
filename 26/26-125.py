with open('26-125.txt') as F:
  D, P = map(int, F.readline().split())
  data = []
  for _ in range(D):
    t, m = map(int, F.readline().split())
    data.append( (t, m) )

data.sort()

freeTime = [0]*P
totalCount = maxCount = 0
for t, m in data:
  if m < 2: continue
  for i, tFree in enumerate(freeTime):
    if t >= tFree:
      if tFree: t += 2
      portions = min( m//2, 60*24-t )
      totalCount += portions
      maxCount = max( portions, maxCount )
      freeTime[i] = t + portions
      #print( i, (t, m), portions, freeTime )
      break
  else:
    continue

print( totalCount, maxCount )