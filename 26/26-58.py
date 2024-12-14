with open('26.txt') as F:
  S, N = map( int, F.readline().split() )
  data = {}
  for i in range(N):
     x = int(F.readline())
     data[x] = data.get(x,0) + 1

data = [[x,c] for x, c in data.items()]
data.sort()

total = 0
maxCount = 0
maxCost = 0
while data and total + 2*data[0][0] <= S:
  # print(data)
  if data[0][1] >= 2:
    k = 2
    while k < data[0][1] and total + (k+1)*data[0][0] <= S:
      k += 1
    print( '>', total, data[0], k )
    total += k*data[0][0]
    maxCost = data[0][0]
    maxCount = max(maxCount, k)
  else:
    k = 1
  if k == data[0][1]:
    del data[0]

print( maxCost, total, S )

total -= maxCost*2
while data and total + 2*data[0][0] <= S:
  if data[0][1] >= 2:
    print( total, data[0], 2 )
    maxCost = data[0][0]
    maxCount = max(maxCount, 2)
  del data[0]

print( maxCost, maxCount )


