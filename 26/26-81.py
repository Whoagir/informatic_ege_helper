with open('26-81.txt') as F:
  N, K = map( int, F.readline().split() )
  data = []
  for i in range(N):
    deck, row, place = map( int, F.readline().split() )
    data.append( (deck, row, place) )

data.sort()

def checkRow( mask ):
  global count, maxRow
  s = ''.join( mask )
  if s[0] == s[-1] == '1' and '0000' in s[1:-1]:
    count += 1
    maxRow = max( maxRow, prevRow[1] )

prevRow = data[0][0:2]
count = maxRow = 0
rowMask = ['0']*K
for i in range(N):
  deck, row, place = data[i]
  if (deck, row) != prevRow:
    checkRow( rowMask )
    rowMask = ['0']*K
  rowMask[place-1] = '1'
  prevRow = (deck, row)

checkRow( rowMask )

print( maxRow, count )