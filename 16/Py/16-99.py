mem = {}
def F( n ):
  if n in mem: return mem[n]
  if n == 0: return 0
  if n < 3: return 1
  res = F(n-1) + F(n-2)
  mem[n] = res
  return res

count = 0
print( F(47) )
