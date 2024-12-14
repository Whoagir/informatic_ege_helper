with open('26-55.txt') as F:
  N, S = map( int, F.readline().split() )
  data = []
  for i in range(N):
     data.append( int(F.readline()) )

data.sort( reverse=True )

count = 1
while True:
  total = 0
  i = 0
  while i < len(data):
    if total + data[i] <= S:
      total += data[i]
      #print( '+', data[i] )
      del data[i]
    else:
      i += 1
  #print( total, i )
  if not data: break
  count += 1
  total = 0

print( count, total )