# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('0123456789', repeat = 5):
    s = ''.join(s)
    if s[0] != '0' and s.count('2') == 1:
        for el in '0468':
            s = s.replace(el, 'Ч')
        if '2Ч' not in s and 'Ч2' not in s:
            k += 1
print(k)
