# Автор? А. Богданов

with open('26-108.txt') as F:
  N, M = map( int, F.readline().split() )
  data = []
  for i in range(N):
    doc, r, m, *fi = map( int, F.readline().split() )
    data.append( (r + m + max(fi), doc) )

data.sort( reverse = True )

# проходной балл - больше, чем у первого непрошедшего,
print( min( ball for ball, doc in data
                 if ball > data[M][0] ) )

data = [ ball for ball, doc in data if doc ]
print( min( ball for ball in data
                 if ball > data[M] ) )
