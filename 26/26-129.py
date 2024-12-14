with open('26-129.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    t1, t2  = map(int, F.readline().split())
    if t1 < t2: # все числа различны
      data.append( (t1, 1, i+1) )
    else:
      data.append( (t2, 2, i+1) )

data.sort()

placed = [0]*N
n1 = 0
n2 = N-1
for t, op, no in data:
  if op == 1:
    placed[n1] = no
    n1 += 1
  else:
    placed[n2] = no
    n2 -= 1

print( data[-1][2],
       n1 if data[-1][1] == 2 else n1-1  )

