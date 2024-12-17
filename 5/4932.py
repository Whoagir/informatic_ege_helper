from itertools import product
a='ТИМАШЕВСК'
comb=product(a)
for i in comb:
    c=0
    s=''.join(i)
    if (s[0]=='Т' or 'М' or 'Ш' or 'В' or 'С' or 'К') and (s[-1]=='Т' or 'М' or 'Ш' or 'В' or 'С' or 'К') and ('ИАЕ' in s or 'ИЕА' in s  or 'ЕАИ' in s  or 'ЕИА' in s or 'АЕИ' in s or 'АИЕ' in s):
        c+=1
print(c)