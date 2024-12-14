with open('26-56.txt') as F:
  V, K, N = map( int, F.readline().split() )
  data = []
  for i in range(N):
     data.append( int(F.readline()) )

data.sort( reverse=True )
space = [V] * K

local = []
i = K-1
while True:
  j = i
  while True:
    j = (j + 1) % K
    if space[j] >= data[0]:
      space[j] -= data[0]
      print(data[0], space)
      break
    if j == i:
      local.append(data[0])
      break
  del data[0]
  if not data: break
  i = j

print( sum(local), len(local) )