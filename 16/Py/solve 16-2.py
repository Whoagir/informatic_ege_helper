memF = {}
def F(n):
  if n <= 1: return 1
  if n in memF: return memF[n]
  val = F(n-1) - 2*G(n-1)
  memF[n] = val
  return val

memG = {}
def G(n):
  if n <= 1: return 1
  if n in memG: return memG[n]
  val = F(n-1) + G(n-1) + n
  memG[n] = val
  return val

for i in range(1,1000+1):
  if abs(F(i)) > 1e9 and abs(G(i)) > 1e9: break
  print(i, F(i), G(i))