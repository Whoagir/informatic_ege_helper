# Автор: PRO100-ЕГЭ

def F( n ):
  return G( n - 1 )
def G( n ):
  return n if n < 10 else \
         G(n-2) + 1

count = 0
for n in range(1,101):
  r = F(n)
  q = round(r**0.5)
  if q > 0 and q*q == r:
    count += 1
print( count )

