from itertools import *
a='ЕСТВО'
comb=product(a,repeat=8)
c=0
for i in comb:
    s=''.join(i)
    gl=s.count('Е')+s.count('О')
    sogl=s.count('С')+s.count('Т')+s.count('В')
    if gl>=3 and sogl>=4 and 'ЕЕ' not in s and 'ЕО' not in s and 'ОО' not in s and 'ОЕ' not in s:
        c+=1
        print(s)
print(c)