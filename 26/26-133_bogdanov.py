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
  if k<=mt:
    mt = k
    mtt = t

p = [0]*M; pk = [0]*M;
for i in range(M):
  for t in range(1500):
    pk[i] += z[i][t]
    p[i] = min(p[i],pk[i])
print(mtt,p.index(min(p))+1)
print(p)
print(pk)

z = [-x+y for x,y in zip(p,pk)]
print(z)
print(min(z),z.index(min(z))+1)
print(max(z),z.index(max(z))+1)
w = [-x for x in p]
print(sum(abs(y-x) for x,y in zip(w,z))/2)
