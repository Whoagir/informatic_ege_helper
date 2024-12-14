with open('26-128.txt') as F:
  N = int(F.readline())
  data = []
  for _ in range(N):
    start, end  = map(int, F.readline().split())
    data.append( (start, end) )

data.sort( key = lambda x: x[1] ) # сортируем по времени окончания

allActions = []
for start, end in data:
  if not allActions or start >= allActions[-1]:
     allActions.append( end )

freeLast = 0
for start, end in data:
  if start >= allActions[-2]:
    freeLast = max( end, freeLast )

print( len(allActions), freeLast )

