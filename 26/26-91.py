with open('26-91.txt') as F:
  N, D = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

data.sort( reverse = True )
data.append( -max(data) )

i, count = 0, 0
while True:
  j = len(data) - 1
  while data[i] + data[j] <= D:
    j -= 1
    if i == j: break
  if data[j+1] > 0:
    count += 1
    # print( data[i], data[j+1] )
    del data[j+1]
    del data[i]
  else:  # переход к следующему по величине пакету
    i += 1
  if i >= len(data)-1: break

print( count, sum(data[:-1]) )





