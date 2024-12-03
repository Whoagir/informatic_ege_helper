# Автор: А. Куканова

from itertools import permutations
CONSONANTS = 'ПЛСН'
LETTERS = 'АПЕЛЬСИН'

count = 0
words = (''.join(w) for w in permutations(LETTERS, r=7))
combos = list((c1 + 'Ь' + c2 for c1 in CONSONANTS for c2 in CONSONANTS if c1 != c2))
print(combos)
print(len(combos))
for w in words:
    if w.count('Ь') == 0 or any(c in w for c in combos):
        count += 1
print(count)

