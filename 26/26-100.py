with open('26-100.txt') as F:
  N, M = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

data.sort( reverse = True )

K = 11
start = 0
while start < N - M:
  trassa = data[start:start+M]
  if all( a - b <= K
          for a, b in zip(trassa, trassa[1:]) ):
     break
  start += 1

end = start + M
while end < N and data[end] == trassa[-1]:
  end += 1

trassa = data[end-M:end]

print( trassa[-1], trassa[0] )


