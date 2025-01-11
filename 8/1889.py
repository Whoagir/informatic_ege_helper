from itertools import *
a='ВУАЛЬ'
comb=permutations(a,r=5)
c=0
for i in comb:
    s=''.join(i)
    if s[0]!='Ь' and 'ЬУ' not in s and 'ЬА' not in s:
        c+=1
print(c)