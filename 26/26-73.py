with open('26-73.txt') as F:
  N = int(F.readline())
  data = [ tuple(map(int, x.split()))
           for x in F.readlines() ]
data.sort()

maxLen = 0
maxLenRow = None
prev = (0, 0)
curLen = 0
for row, pos in data:
  if row == prev[0] and \
     pos in (prev[1], prev[1]+1):
    if pos > prev[1]: curLen += 1
    if curLen >= maxLen:
      maxLen = curLen
      maxLenRow = row
  else:
    curLen = 1
  prev = (row, pos)

print( maxLen, maxLenRow )

