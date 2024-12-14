with open('26-145.txt') as F:
  N = int(F.readline())
  M, K = map( int, F.readline().split() )
  data = []
  for _ in range(N):
    n, kids = map( int, F.readline().split() )
    data.append( (n, kids) )

data.sort( reverse = True )

freePlace = [(K, K, 6*K)]*M
totalKids = 0
for n, kids in data:
  for i in range(M):
    f4, f2, fPlaces = freePlace[i]
    found = False
    if f4 > 0:
      found, f4 = True, f4-1
    elif n <= 2 and f2 > 0:
      found, f2 = True, f2-1
    if found:
      totalKids += kids
      freePlace[i] = (f4, f2, fPlaces-n)
      break

print( totalKids )
free = [ fPlaces for f4, f2, fPlaces in freePlace ]
print( free.index( max(free) ) + 1 )