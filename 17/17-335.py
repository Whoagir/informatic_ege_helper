# Автор: И. Кушнир

a = [ int(i) for i in open("17-335.txt") ]

M = min( [ i for i in a if i % 43 == 0 ] )

mas = []
mas2 = []
for i in range(len(a)-1):
  cond1 = (a[i] + a[i+1]) % M == 0
  cond2 = a[i] % 10 == M % 10 or a[i+1] % 10 == M % 10
  if cond1 ^ cond2: # Другой вариант: int(cond1) + int(cond2) == 1:
    mas.append( max(a[i], a[i+1]) )

print( len(mas), max(mas) )