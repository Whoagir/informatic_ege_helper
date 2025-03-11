from itertools import *
a='КОЛУН'
c=0
comb=permutations(a,r=5)
for i in comb:
    s=''.join(i)
    if 'ОУ' not in s and 'УО' not in s and 'КЛ' not in s and 'КН' not in s and 'ЛК' not in s and 'ЛН' not in s and 'НК' not in s and 'НЛ' not in s:
        c+=1
print(c)