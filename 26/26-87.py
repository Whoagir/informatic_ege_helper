with open("26-87.txt") as F:
  N = int( F.readline() )
  data = []
  for i in range(N):
    r, c, color = F.readline().split()
    data.append( (int(r), int(c), color ) )

def isBlue( data, row, col ):
  return data[0] == row and data[2] == '#0000FF' and \
         abs(data[1] - col) <= 3
def isGreen( color ):
  return color == '#00FF00'

data.sort()

count, rowCount = 0, 0
maxInRow, maxRow = 0, 0
prevRow = -1
for i in range(3, N-1-3):
  row, col, color = data[i]
  if row != prevRow:
    rowCount = 0
  if isGreen(color) and isBlue(data[i-3], row, col) and \
     isBlue(data[i-2], row, col) and isBlue(data[i-1], row, col) and \
     isBlue(data[i+1], row, col) and isBlue(data[i+2], row, col) and \
     isBlue(data[i+3], row, col):
     count, rowCount = count + 1, rowCount + 1
     if rowCount >= maxInRow:
        maxInRow = rowCount
        maxRow = row
  prevRow = row

print( count, maxRow )

