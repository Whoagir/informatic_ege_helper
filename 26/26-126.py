with open('26-126.txt') as F:
  M, K, N = map(int, F.readline().split())
  data = []
  for _ in range(N):
    start, end  = map(int, F.readline().split())
    data.append( (start, end) )

data.sort( key = lambda x: (x[0], -x[1]) )

places = [0]*K
countOK = 0
countFull = 0
prevFull = 0
k = 0
for pos in range(1,M+1):
  for i in range(K):
    if places[i] == pos:
       places[i] = 0
  while k < N and data[k][0] == pos:
    for i in range(K):
      if places[i] == 0:
        places[i] = data[k][1]
        countOK += 1
        break
    k += 1
  if places.count(0) == 0:
    countFull += 1

print( countOK, countFull )

