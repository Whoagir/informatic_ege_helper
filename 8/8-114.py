# Автор: Михлин Б.С.
'''
8.114 Петя составляет четырёхбуквенные слова перестановкой букв слова АБАК.
При этом он избегает слов с двумя подряд одинаковыми буквами.
Сколько всего различных слов может составить Петя?
'''
from itertools import *
# множество автоматически удаляет дубликаты при перестановках букв "А"
P = {p for p in permutations('АБАК') if 'АА'not in ''.join(p)}
print(len(P))  # Ответ: 6

# Примечание: Абак - семейство счётных досок, применявшихся для арифметических вычислений в Древней Греции,
# Древнем Риме и Древнем Китае. Абак - предшественник русских счётов и японского соробана.
