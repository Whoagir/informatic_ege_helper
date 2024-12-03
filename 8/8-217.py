# Автор: А. Куканова

from itertools import product

WORD = 'ЧОАНИМЕ'
count = 0
for k in range(4, 7):
    words = [w for w in product(WORD, repeat=k) if w.count('М') == 3]
    count += len(words)
print(count)