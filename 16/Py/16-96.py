def F(n):
  if n < 10: return n
  return n % 10 + F(n//10)
def G(n):
  if n < 10: return n
  return G(F(n))

sF = sG = 0
for x in range(10,100):
  sF += F(x)
  sG += G(x)

print( sF, sG )