# Автор: А. Куканова

from itertools import product

count = 0
for w in product('ПИТОН', repeat=4):
    if (all(w[i] in 'ПТН' for i in (0, 2)) and all(w[i] in 'ИО' for i in (1, 3))
            or all(w[i] in 'ИО' for i in (0, 2)) and all(w[i] in 'ПТН' for i in (1, 3))):
        count += 1
print(count)