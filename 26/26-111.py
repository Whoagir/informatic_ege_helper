with open('26-111.txt') as F:
  K = int(F.readline())
  N = int(F.readline())
  data = []
  for _ in range(N):
    t0, tEnd = map(int, F.readline().split())
    data.append( (t0, tEnd) )

data.sort()

tFree = [0]*K

lastStart = 0
count = 0
for t0, tEnd in data:
  for k in range(K):
    if t0 > tFree[k]:
      count += 1
      tFree[k] = tEnd
      if t0 > lastStart:
        lastStart = t0
        kLast = k
      break

print( count, kLast + 1 )
