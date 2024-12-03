# Автор: А. Куканова

from itertools import permutations

words = set(permutations('МИМИКРИЯ', r=8))
print(len(words))

