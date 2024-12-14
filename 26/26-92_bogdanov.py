# Автор: А. Богданов

f = open('26-92.txt')
n = int(f.readline())
d = set()
for i in range(n):
  s = f.readline()
  r,c,z = map(int, (s.strip()+'1').split())
  if z<0:
    d.discard((r,c))
  else:
    d.add((r,c))

d = sorted(d)
k = mx = 1
rx = None
for i in range(1,len(d)):
  r1,c1 = d[i-1]
  r2,c2 = d[i]
  if r1==r2 and c2-c1==1:
    k += 1
    #if 3859 <= r1 <= 3862:
    #  print( k, r1, c2 )
    if k>=mx:
      mx,rx = k,r1
  else:
    k = 1
print(mx,rx)

for r, c in [ (r,c) for r, c in d if r == 3861 ]:
  print( r, c )

