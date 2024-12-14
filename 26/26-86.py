with open('26-86.txt') as F:
   N = int(F.readline())
   data = []
   for i in range(N):
     data.append( tuple(map(int, F.readline().split())) )

data.sort()

times = {}
endTimes = []
for time, pos in data:
  times[pos] = times.get( pos, [] ) + [time]
  if len(times[pos]) % 2 == 0:
    endTimes += [time]

intervals = { pos: [ arr[i]-arr[i-1] for i in range(1,len(arr), 2) ]
              for pos, arr in times.items() }

maxInHour = 0
M = len(endTimes)
for i, start in enumerate(endTimes):
  count = 0
  for j in range(i, M):
    if endTimes[j] >= start+60: break
    count += 1
  if count > maxInHour:
    maxInHour = count

avgByPos = { pos: sum(arr)/len(arr)
             for pos, arr in intervals.items() if len(arr) > 0 }
maxAvg = max( list(avgByPos.items()), key = lambda x: x[1]  )

print( maxInHour, maxAvg[0] )


