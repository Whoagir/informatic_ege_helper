# Автор: А. Куканова

from itertools import product

WORD = 'ПСКАЛЬ'
words = [''.join(w) for w in product(WORD, repeat=4)]
words = [w for w in words if w[0] != 'Ь' and 'ЬЬ' not in w]
print(len(words))
