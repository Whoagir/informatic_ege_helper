# Автор: А. Куканова

from itertools import permutations

words = set(permutations('ТИКТОК', r=6))
words = [w for w in words if all(w[i] != w[i+1] for i in range(5))]
print(len(words))