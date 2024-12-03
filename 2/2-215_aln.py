#2.215_2_vars  Автор А.Л.Наймушин
print('Классический вариант с циклом')
print ('a b c d') # заголовок таблицы (в алфавитном порядке)
k = 0, 1          # k - кортеж констант (0 - False, 1 - True)
for a in k:
  for b in k:
    for c in k:
      for d in k:
        if not ((a and (not b)) or(a or b) and c or d):
            print(a, b, c, d) # если F = 0
'''
Классический вариант с циклом
a b c d
0 0 0 0
0 0 1 0
0 1 0 0
1 1 0 0
'''
print('Вариант с модулем itertools')
from itertools import product
print ('a b c d') # заголовок таблицы (в алфавитном порядке)
for a, b, c, d in product([0, 1], repeat=4):
  if not ((a and (not b)) or(a or b) and c or d):
            print(a, b, c, d) # если F = 0
'''
Вариант с модулем itertools
a b c d
0 0 0 0
0 0 1 0
0 1 0 0
1 1 0 0
'''
