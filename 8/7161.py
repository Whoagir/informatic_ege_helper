from itertools import product, repeat

a='БЕЧЮ'
comb=product(a,repeat=5)
c=0
res=0
for  i in comb:
    s=''.join(i)
    c+=1
    if s[0]!='Ю' and (not('ЕЕ' in s)) and c%2==0:
        res+=1
print(res)