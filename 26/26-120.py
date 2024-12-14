with open('26-120.txt') as F:
  M, N = map( int, F.readline().split() )
  L = list(map( int, F.readline().split() ))
  data = []
  for _ in range(N):
    start, t, typ = map(int, F.readline().split())
    data.append( (start, start+t, typ) )

data.sort()

sumL = sum(L)
busyUntil = [0]*sumL
p = [0]*(M+1)
for i in range(1,M+1):
  p[i] = p[i-1] + L[i-1]

count = [0]*M
countFail = 0
for start, end, typ in data:
   place0 = p[typ]
   for place in range(place0, sumL):
     if start >= busyUntil[place]:
       busyUntil[place] = end
       count[typ] += 1
       # print( i, typ, place )
       break
   else:
     countFail += 1

K = max( i for i in range(M) if count[i] == max(count) )
tFreeK = max( busyUntil[place]
              for place in range(p[K], sumL) )

print( tFreeK, countFail )