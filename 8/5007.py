from itertools import product
a='АТТЕСТАТ'
comb=product(a,repeat=8)
c=0
for i in comb:
    s=''.join(i)
    if s.count('А')==2 and s.count('Т')==4 and s.count('Е')==1 and s.count('С')==1 and ('АА' in s or 'ТТ' in s or 'ЕА'in s or 'АЕ' in s or 'ТС' in s or 'СТ' in s):
        c+=1
print(c)