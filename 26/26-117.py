with open('26-117.txt') as F:
  K, N = map( int, F.readline().split() )
  data = [ tuple(map(int, F.readline().split())) for i in range(N) ]

data.sort()
freeTime = [0]*K # время готовности
maxWait = 0
lastRoom = -1
for tStart, tEnd in data:
  k = 0
  for i in range(1, K):
    if freeTime[i] <= freeTime[k]: k = i
  if freeTime[k] <= tEnd and freeTime[k] < 7*24*60:
    maxWait = max( freeTime[k] - tStart, maxWait )
    #print( tStart, tEnd, '->', k+1, max(0,freeTime[k] - tStart) )
    freeTime[k] = max( freeTime[k], tEnd ) + 31
    lastRoom = k + 1

print( maxWait, lastRoom )



