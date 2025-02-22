from itertools import *
a='ЕЛЙ'
c=0
comb=product(a,repeat=6)
for i in comb:
    s=''.join(i)
    v=s.count('Й')
    if v<=1 and s[0]!='Й' and s[-1]!='Й' and 'ЙЕ' not in s and 'ЕЙ' not in s:
        c+=1
print(c)