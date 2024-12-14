with open('26-73.txt') as F:
  N = int(F.readline())
  data = [ tuple(map(int, F.readline().split()))
           for i in range(N) ]

data.sort()

maxLen = 0
maxLenRow = None
for row in range(1,640+1):
  dRow = [ x[1] for x in data if x[0] == row ]
  prev = -100
  maxLen1 = curLen = 0
  for pos in dRow:
    if pos in (prev, prev+2):
      if pos > prev: curLen += 2
      if curLen//2+1 > maxLen1:
        maxLen1 = curLen//2 + 1
    else:
      curLen = 1
    prev = pos
  if maxLen1 > maxLen:
    maxLen = maxLen1
    maxLenRow = row

print( maxLen, maxLenRow )

