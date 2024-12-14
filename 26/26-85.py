with open('26-85.txt') as F:
  N = int( F.readline() )
  data = [ tuple(map(int, F.readline().split()))
           for i in range(N) ]

# countFree, count0 = 3, 2
countFree, count0 = 100, 500

data.sort()
data.append( (0, 0, 0) ) # барьер

def appendRow( s, col, where ):
  if len(s) < col:
    s += ' '*(col - len(s))
  s += '0' if where == 0 else '1'
  return s

def valid( s ):
  chunks = s.split('1')
  return any( ch == ' '*countFree for ch in chunks ) and \
         s.count('0') >= count0

i = 0
specRow, countN = None, None
while i < N:
  row = data[i][0]
  s = ''
  while data[i][0] == row:
    s = appendRow( s, data[i][1], data[i][2] )
    i += 1
  if valid( s ):
    specRow = row
    countN = s.count('1')

print( specRow, countN )



