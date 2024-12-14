with open('26-92.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    r, c, mode = F.readline().rstrip().split()
    data.append( ( int(r), i, int(c), mode ) )

data.sort()

M = 10000

def check( r, rowData ):
  global bestRow, maxCount
  count = cur = 0
  for i in range(M):
    if rowData[i] == '1':
       cur += 1
       count = max(cur, count)
    else:
       cur = 0
  if count >= maxCount:
    maxCount = count
    bestRow = r

bestRow, maxCount = None, 0
prevRow, rowData = None, ['0']*M
for i in range(N):
  r, _, c, mode = data[i]
  if r != prevRow:
    check( prevRow, rowData )
    rowData = ['0']*M
  rowData[c-1] = '1' if mode == '+' else '0'
  prevRow = r

check( r, rowData )

print( maxCount, bestRow )

