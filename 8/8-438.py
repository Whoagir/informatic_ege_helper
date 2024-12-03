# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('012345678', repeat = 6):
    s = ''.join(s)
    if s[0] != '0' and s.count('4') == 1:
        for el in '1357':
            s = s.replace(el, 'Н')
        if '4Н' not in s and 'Н4' not in s:
            k += 1
print(k)
