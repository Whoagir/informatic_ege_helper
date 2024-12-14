# Автор: А. Богданов

(M,N), *a = [list(map(int,s.split())) for s in open('26-123.txt')]
a = a[:N]

a.sort()

z = [[0]*1500 for _ in range(M)]
for t,dt,x,y in a:
  z[x-1][t] -= 1
  z[y-1][t+dt] += 1

k = mt = 0
for t in range(1500):
  for i in range(M):
    k += z[i][t]
  mt = min(mt,k)

p = [0]*M
for i in range(M):
  k = 0
  for t in range(1500):
    k += z[i][t]
    p[i] = min(p[i],k)
print(-sum(p),-mt)
