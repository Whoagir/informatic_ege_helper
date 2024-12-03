# Автор: А. Куканова

from itertools import permutations

WORD = 'КУСАТЬ'
words = [''.join(w) for w in permutations(WORD, r=5)]
words = [w for w in words if w[0] != 'Ь' and 'СУК' not in w]
print(len(words))