with open("26-148.txt") as F:
  N = int(F.readline())
  data = []
  maxRow = 0
  for s in F:
    row, place = map(int, s.split())
    data.append( (row, place) )
    maxRow = max(row, maxRow)

data.sort()

for row in range(maxRow, 0, -1):
  placesInRow = [ p for r, p in data if r == row ]
  if placesInRow:
    placesInRow.insert( 0, 0 )
    found = False
    for i in range(len(placesInRow)-1):
      if placesInRow[i+1] - placesInRow[i] > 5:
        found = True
        break
    if found:
      if placesInRow[i] == 0:
        print( row, placesInRow[i+1]-5 )
      else:
        print( row, placesInRow[i]+1 )
      break

# Автор: Е. Джобс

data.sort( key=lambda x: (-x[0], x[1]) )

last = [-1, -1]
for row, num in data:
  if last[0] != row and num >= 6:
    print( row, num-5 )
    break
  if last[0] == row and num - last[1] >= 6:
    print( row, last[1]+ 1  )
    break
  last = row, num
