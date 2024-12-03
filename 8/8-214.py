# Автор: А. Куканова

from itertools import permutations
count = 0
for w in (''.join(w) for w in permutations('ВАЙФУ', r=4)):
    if w[0] != 'Й' and 'ВФ' not in w and 'ФВ' not in w:
        count += 1
print(count)