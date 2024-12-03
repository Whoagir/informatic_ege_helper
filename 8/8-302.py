from itertools import product

count = 0
for n in set(product( 'КОМПЬЮТЕР', repeat=6 )):
  n = ''.join(n)
  posK = n.find('К')
  posT = n.rfind('Т')
  if posK >= 0 and posT >= 0:
    for i in range(posK+1, posT):
       if n[i] == 'О':
         count += 1
         break

print( count )