with open('26-119.txt') as F:
  N, L, M = map( int, F.readline().split() )
  data = []
  for _ in range(N):
    start, t, typ = F.readline().split()
    start, t = int(start), int(t)
    data.append( (start, start+t, typ) )

data.sort()

busyUntil = [0]*(L+M)
countB = countFail = 0
i = 0
for start, end, typ in data:
   place0 = 0 if typ == 'A' else L
   for place in range(place0, L+M):
     if start >= busyUntil[place]:
       busyUntil[place] = end
       # print( i, typ, place )
       countB += (typ == 'B')
       break
   else:
     countFail += 1
   i += 1

print( countB, countFail )

