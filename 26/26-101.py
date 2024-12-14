with open("26-101.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

data.sort( reverse = True )

blocks = []
while data:
  maxCube = prev = data.pop( 0 )
  k = 1
  i = 0
  while i < len(data):
    if prev - data[i] >= K:
      prev = data.pop( i )
      k += 1
    else:
      i += 1
  blocks.append( (maxCube, k) )

print( len(blocks), max(blocks, key = lambda x: x[1])[1] )