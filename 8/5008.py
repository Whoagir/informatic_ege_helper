from itertools import *
a='ВОЛКДА'
a1='ВЛКД'
c=0
v=[]
comb=product(a,repeat=8)
combs=product(a1,repeat=2)
for j in combs:
    s1=''.join(j)
    v.append(s1)
for i in comb:
    s=''.join(i)
    if s.count('В')==2 and s.count('О')==2 and s.count('Л')==1 and s.count('К')==1 and s.count('Д')==1 and s.count('А')==1:
        if 'ОО' in s or 'ОА' in s or 'АО' in s or 'АА' in s  or 'ВВ' in s or 'ВЛ' in s or 'ВК' in s or 'ВД' in s or 'ЛВ' in s or 'ЛЛ' in s or 'ЛК' in s or 'ЛД' in s or 'КВ'in s or 'КЛ' in s or 'КК' in s or 'КД' in s or 'ДВ' in s or 'ДЛ'in s or 'ДК' in s or'ДД' in s:
            c+=1
print(v)
print(c)