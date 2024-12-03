# Автор: А. Куканова

from itertools import product

WORD = 'ПИКАЧУ'
words = [w for w in product(WORD, repeat=5) if w.count('У') >= 2]
print(len(words))