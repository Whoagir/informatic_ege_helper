# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('01234567', repeat = 5):
    s = ''.join(s)
    if s[0] != '0' and s.count('3') <= 1:
        for el in '1357':
            s = s.replace(el, 'Н')
        if 'НН' not in s:
            k += 1
print(k)
