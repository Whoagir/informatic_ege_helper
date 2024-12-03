# Автор: Михлин Б.С.
'''
8.118 Петя составляет шестибуквенные слова перестановкой букв слова АВРОРА.
При этом он избегает слов с двумя подряд одинаковыми буквами.
Сколько всего различных слов может составить Петя?
'''
from itertools import *
P = {p for p in map(''.join, permutations('АВРОРА')) if 'АА' not in p and 'РР' not in p}
#P={p for p in permutations('АВРОРА') if 'АА' not in ''.join(p) and 'РР' not in ''.join(p)}
print(len(P))  # Ответ: 84
