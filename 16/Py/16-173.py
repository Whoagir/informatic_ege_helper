def F( n ):
  return n if n < 10 else F(G(n))
def G( n ):
  return F(n) if n < 10 else G(n//10) + G(n%10)

a, b = 10, 20
for i in range(5):
  count = 0
  for n in range(a, b):
    if F(n) == 3:
      count += 1
  print( f"[{a};{b}] => {count}" )
  a, b = a*10, b*10

print( "...\n[100000000;200000000] => 11111111" )
