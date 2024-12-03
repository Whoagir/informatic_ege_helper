# Михлин Б.С.
'''
2.282 (ЕГЭ-2024) Логическая функция F задаётся выражением 
(not x and y and z and not w) or (not x and y and not z and not w) or (x and y and z and not w).
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w. 
?	?	?	?	F
1				1
0		1		1
	0	0		1
В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы.
Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.
'''
# Из формулы и таблицы сразу видно, что "w" не может равняться 1, т.е. это 2-я или 4-я колонка

def f(x, y, w, z):
    return (not x and y and z and not w) or (not x and y and not z and not w) or (x and y and z and not w)
    # return ((not x and y and z ) or (not x and y and not z) or (x and y and z)) and not w

from itertools import *
for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    t = [(1, a1, a2, a3), (0, a4, 1, a5), (a6, 0, 0, a7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p, sep='')  # Ответ: xwzy
