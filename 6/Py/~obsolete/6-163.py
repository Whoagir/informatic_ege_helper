G = 253729
n0 = 1531
target = 526
dx = 3
dn = 7
kMax = ((target+1)*1000 - 1 - n0) // dn
nMax = n0 + kMax*dn
x0 = G*1000 - nMax + kMax*dx

print(x0)

x0 = x0 - 10

res = []
while True:
  x = x0
  n = n0
  while (x+n)//1000 < G:
    x -= dx
    n += dn
  #print( n//1000 )
  if n//1000 == target:
    res.append( x0 )
  if n//1000 < target:
    break
  x0 += 1

print( min(res), max(res) )