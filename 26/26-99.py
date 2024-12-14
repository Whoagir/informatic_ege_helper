with open('26-99.txt') as F:
  N, M = map( int, F.readline().split() )
  data = []
  for i in range(N):
    data.append( int(F.readline()) )

data.sort( reverse = True )

autos = []
while data:
  total = 0
  for weight in data[:]:
    if total + weight <= M:
      total += weight
      data.remove( weight )
  autos.append( total )

print( len(autos), autos[-2] )


