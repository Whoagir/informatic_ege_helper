# Автор: А. Куканова

from itertools import permutations

LETTERS = 'КЛАБХАУС'
words = set(permutations(LETTERS, r=len(LETTERS)))
words = [w for w in words if all(w[i] != w[i+1] for i in range(len(w) - 1))]
print(len(words))