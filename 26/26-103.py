with open("26-103.txt") as F:
  N, K, M = map( int, F.readline().split() )
  data = []
  for _ in range(N):
    size, type = F.readline().strip().split()
    data.append( (int(size), ord(type)) )

data.sort( reverse = True, key=lambda x: (x[0], -x[1]) )

blocks = []
while data:
  maxCube = prev = data.pop( 0 )
  k = 1
  i = 0
  #print( '*', prev )
  while i < len(data):
    if prev[0] - data[i][0] >= K and prev[1] != data[i][1]:
      prev = data.pop( i )
      #print( prev )
      k += 1
      if k == M: break
    else:
      i += 1
  blocks.append( (maxCube, k) )

print( len(blocks), sum( 1 for b in blocks if b[1] == M ) )
