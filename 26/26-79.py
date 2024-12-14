with open("26-79.txt") as F:
  N, K = map(int, F.readline().split())
  data = []
  for i in range(N):
    p = tuple(map(int, F.readline().split()))
    data.append(p)

data.sort()

row = pos = None
for i in range(1,N):
  if data[i-1][0] == data[i][0] and \
     data[i][1] == data[i-1][1] + K + 1:
     if data[i][0] != row:
       row = data[i][0]
       pos = data[i-1][1] + 1

print( row, pos )