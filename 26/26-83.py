with open('26-82.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    row, pos = map( int, F.readline().split() )
    data.append( (row, pos) )

data.sort()

maxRow = maxCount = 0
prevRow = -1
for row, pos in data:
  if row != prevRow:
    rowTargets = set()
  if pos % 2 == 1:
    rowTargets.add( pos )
    count = len(rowTargets)
    if count > maxCount:
      maxCount, maxRow = count, row
      print( row, count )
  prevRow = row

print( maxCount, maxRow )