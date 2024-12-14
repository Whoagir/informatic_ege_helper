with open('26-130.txt') as F:
  N = int(F.readline())
  count = [0]*1440
  for i in range(N):
    t1, t2  = map(int, F.readline().split())
    for t in range(t1, t2+1):
      count[t] += 1

peakValue = max(count)

numPeaks = 0
for i in range(1,1440):
  if count[i] == peakValue and count[i] > count[i-1]:
    numPeaks += 1

print( numPeaks, peakValue  )

