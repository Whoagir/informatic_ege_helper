def F(n):
  if n < 10: return n
  return F(G(n))
def G(n):
  if n < 10: return n
  return n%10 + G(n//10)

sF = sG = 0
for x in range(10,100):
  sF += F(x)
  sG += G(x)

print( F(12345678987654321) )