# Автор: А. Куканова

from itertools import product

WORD = 'ИНФА'
words = [w for w in product(WORD, repeat=6) if w.count('Ф') == 2]
print(len(words))