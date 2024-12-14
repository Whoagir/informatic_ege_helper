with open("26-102.txt") as F:
  N, K = map( int, F.readline().split() )
  data = []
  for _ in range(N):
    size, type = F.readline().strip().split()
    data.append( (int(size), type) )

data.sort( reverse = True )

blocks = []
while data:
  maxCube = prev = data.pop( 0 )
  k = 1
  i = 0
  while i < len(data):
    if prev[0] - data[i][0] >= K and prev[1] != data[i][1]:
      prev = data.pop( i )
      k += 1
    else:
      i += 1
  blocks.append( (maxCube, k) )

print( len(blocks), max(blocks, key = lambda x: x[1])[1] )