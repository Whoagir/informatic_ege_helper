from itertools import *
a='ЕСАУЛ'
comb=permutations(a)
c=0
for i in comb:
    s=''.join(i)
    if 'ЕЕ' not in s and 'ЕА' not in s and 'АЕ' not in s and 'ЕУ' not in s and 'УЕ' not in s and 'АА' not in s and 'АУ' not in s and 'УА' not in s and 'УУ' not in s:
        c+=1
        print(s,c)