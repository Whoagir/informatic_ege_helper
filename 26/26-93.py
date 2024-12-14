with open('26-93.txt') as F:
  N, M = map( int, F.readline().split() )
  data = []
  for i in range(N):
    floor, pos = map( int, F.readline().split() )
    data.append( (floor, pos) )

data.sort()
MAXLEN = 5000

def checkFloor( mask ):
  global count, maxFloor
  for i in range(1,MAXLEN):
    neighbours = 0
    j = i - 1
    while j > 0 and mask[j]:
      neighbours += 1
      j -= 1
    k = i + 1
    while k < MAXLEN-1 and mask[k]:
      neighbours += 1
      k += 1
    if neighbours >= M:
      count += 1
      print( count, ':', prevFloor, i, mask[j+1:k] )
      maxFloor = prevFloor
  # print( prevFloor, count, mask )

prevFloor = 0
count = maxFloor = 0
floorMask = [0]*(MAXLEN+1)
for i in range(N):
  floor, pos = data[i]
  if floor != prevFloor:
    checkFloor( floorMask )
    floorMask = [0]*(MAXLEN+1)
  floorMask[pos] = 1
  prevFloor = floor

checkFloor( floorMask )

print( count, maxFloor )