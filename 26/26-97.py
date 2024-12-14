with open('26-97.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    D, S = map(int, F.readline().split())
    data.append( (D-2*S-3, D, S) )

data.sort( reverse = True )

package, nextD = [], 10**10
for tube in data:
  if tube[1] <= nextD:
    package.append( tube )
    nextD = tube[0]

data.sort( key = lambda x: x[1],
           reverse = True )

package.pop()
nextD = package[-1][0]
for tube in data:
  if tube[1] <= nextD:
    package.append( tube )
    break

print( len(package), package[-1][1] )
