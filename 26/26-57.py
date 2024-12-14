with open('26-57.txt') as F:
  N, M = map( int, F.readline().split() )
  data = []
  for i in range(N):
     data.append( int(F.readline()) )

data.sort( reverse=True )

count = 0
while sum(data) >= M:
  part = data[0]
  i = 1
  while i < len(data) and part + data[i] <= M:
    part += data[i]
    count += 1
    i += 1
  if i == len(data):
    break
  # print( data[:i], sum(data[:i]), end=" " )
  del data[:i]
  if part < M:
    i = len(data) - 1
    while part + data[i] < M:
      i -= 1
    part += data[i]
    # print( data[i], end=" " )
    count += 1
    if part > M:
      data.append( part - M )
      # print( '->', part - M )
    del data[i]
    data.sort( reverse = True )
  # print()

print( count, len(data) )


