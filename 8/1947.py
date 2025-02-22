from itertools import *
a='АЙСБЕРГ'
c=0
comb=permutations(a,r=7)
for i in comb:
    s=''.join(i)
    if s[0]!='Й' and 'ЙА' not in s and 'ЙЕ' not in s:
        c+=1
print(c)