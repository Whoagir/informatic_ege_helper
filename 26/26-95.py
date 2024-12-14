with open('26-95.txt') as F:
  N = int( F.readline() )
  data = []
  for i in range(N):
    house, entry = map( int, F.readline().split() )
    data.append( (house, entry) )

M = 3
data.sort()
MAXLEN = 5000

def checkHouse( mask ):
  global count, minEntry
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
      print( count, ':', prevHouse, i, mask[j+1:k] )
      minEntry = i
      return
  # print( prevhouse, count, mask )

prevHouse = 0
count = minEntry = 0
houseMask = [0]*(MAXLEN+1)
for i in range(N):
  house, entry = data[i]
  if house != prevHouse:
    checkHouse( houseMask )
    houseMask = [0]*(MAXLEN+1)
  houseMask[entry] = 1
  prevHouse = house

checkHouse( houseMask )

print( count, minEntry )