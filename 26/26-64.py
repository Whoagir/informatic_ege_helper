target = 'A'

with open("26-64.txt") as F:
  N, M = map( int, F.readline().split() )
  data = []
  for i in range(N):
    d = F.readline().split()
    data.append( (int(d[0]), d[1]) )

data.sort()
print( data )

# определяем максимальное общее число деталей
count, S = {}, 0
for i in range(N):
  v, m = data[i]
  if S+v <= M:
    iLast = i
    S += v
    print(v, m)
    count[m] = count.get(m, 0) + 1

# пытаемся увеличить количество target
remainingA = [ (v, m) for v, m in data[iLast+1:]
                        if m == target ]

i = iLast
while remainingA and i >= 0:
  v, m = data[i]
  if m != target:
    vA, mA = remainingA.pop(0)
    if S - v + vA <= M:
      count[target] = count.get(target, 0) + 1
      S = S - v + vA
      print( i, '*', -v, m, '<-', vA, mA, ':', M - S )
    else:
      break
  i -= 1

print( count[target], M - S  )