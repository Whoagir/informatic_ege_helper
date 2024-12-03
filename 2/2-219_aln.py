#2.219_Автор_А_Наймушин

from itertools import product
print ('x y w z') # заголовок таблицы (в алфавитном порядке)
for x, y, w, z in product([0, 1], repeat=4):
  if not ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and not x)):
    print(x, y, w, z) # если F = 0

'''
x y w z
0 0 1 0
1 0 1 0
1 1 0 1
1 1 1 0

'''
