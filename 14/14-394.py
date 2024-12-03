
for x in range(36):
  n1 = 1*36**4 + 2*36**3 + x*36**2 + 4*36 + 5
  n2 = 1*12345 + x
  if (n1 + n2) % 13 == 0:
    print( x, (n1+n2)//13 )

# Автор: А. Богданов

for x in '0123456789abcdefghijklmnopqrstuvwxyz':
  r = int(f'12{x}45',36)+1*12345+int(x,36)
  if r%13==0:
    print(x,r,r//13)
