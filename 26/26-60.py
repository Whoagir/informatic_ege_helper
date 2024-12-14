with open('26-60.txt') as F:
  K, N = map( int, F.readline().split() )
  specMax = []
  for i in range(K):
    specMax.append( int(F.readline()) )
  abitur = []
  for pos in range(N):
    ball, code = map( int, F.readline().split() )
    abitur.append( (ball, code) )

abitur.sort( reverse = True )
count = 0
minBall = [0]*K
accepted = [0]*K
total = [0]*K
for a in abitur:
  code = a[1]
  total[code] += 1
  if accepted[code] < specMax[code]:
    accepted[code] += 1
    minBall[code] = a[0]
    count += 1

rate = [ total[code]/specMax[code]
         for code in range(K) ]

print( count )
print( minBall[rate.index(max(rate))] )



