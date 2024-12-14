with open('26-151.txt') as F:
  N, S = [int(x) for x in F.readline().split()]
  data = []
  for i in range(N):
    ID, o1, o2, o3, sobes = map( int, F.readline().split() )
    data.append( (o1+o2+o3, sobes, -ID) )

data.sort( reverse = True )
#print(data)

last = data[S-1]
print( last )
if last[0] > data[S][0]: # нет полупроходного балла
  print( -last[2], 0 )
else:
  halfPass = last[0]
  iLastPass = S - 2
  while data[iLastPass][0] == last[0]:
    iLastPass -= 1
  print( -data[iLastPass][2],
         len([ d for d in data if d[0] == halfPass ] ) )