with open('26-110.txt') as F:
  N = int(F.readline())
  data = []
  for _ in range(N):
    row, pos = map( int, F.readline().split() )
    data.append( (row, pos) )

data.sort()
data.append( (100000, 0) ) # барьер

D = 10
maxLen = curLen = 0
ro, co = -1, -1
for r, c in data:
  if r != ro:
    curLen = 1
  else:
    if c - co <= D + 1:
      curLen += c - co
      if curLen > maxLen:
        maxLen, maxRow = curLen, r
    else:
      curLen = 1
  ro, co = r, c

print( maxLen, maxRow )
