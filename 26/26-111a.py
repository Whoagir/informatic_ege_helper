with open('26-111.txt') as F:
  K = int(F.readline())
  N = int(F.readline())
  data = []
  for _ in range(N):
    start, end = map(int, F.readline().split())
    data.append( (start, end) )

data.sort()
#print( data )

def take( i, pos ):
  global tFree, count, lastStart, iLast
  tFree = data[pos][1] + 1
  #print( data[pos] )
  if data[pos][0] > lastStart:
    lastStart, iLast = data[pos][0], i
  del data[pos]
  count += 1

count = 0
lastStart, iLast = 0, -1
for i in range(K):
  # все для i-й ячейки
  take( i, 0 )
  j = 0
  while j < len(data):
    while j < len(data):
      if data[j][0] >= tFree: break
      j += 1
    if j < len(data):
      take( i, j )

print( count, iLast + 1 )
