# Автор: А. Куканова

from itertools import product

WORD = 'ЗЕРКАЛО'
words = [''.join(w) for w in product(WORD, repeat=6)]
words = [w for w in words if 1 <= w.count('К') <= 4 and len(set(w)) == 6 - w.count('К') + 1]
print(len(words))