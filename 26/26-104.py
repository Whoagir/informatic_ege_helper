
F = open("26-104.txt")
N, K = map( int, F.readline().split() )

data = {}
for _ in range(N):
  row, pos = map(int, F.readline().split())
  if row in data:
    data[row].append( pos )
  else:
    data[row] = [pos]

F.close()

def countLines( rowData ):
  count = 0
  prev, L = -100, 0
  for pos in sorted(set(rowData)):
    if pos == prev + 1:
      L += 1
    else:
      if L >= K: count += 1
      L = 1
    prev = pos
  if L >= K: count += 1
  return count

bestRow = (0, 0)
for row in sorted(data):
  count = countLines( data[row] )
  if count >= bestRow[0]:
    bestRow = ( count, row )
    print( row, count )

print( *bestRow )
