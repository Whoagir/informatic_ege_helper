# Автор: А. Куканова

from itertools import permutations

WORD = 'ТЬЮРИНГ'
VOWELS = 'ЮИ'
words = [''.join(w) for w in permutations(WORD, r=6)]
words = [w for w in words if not(w[0] == 'Ь' or any(v + 'Ь' in w for v in VOWELS))]
print(len(words))
