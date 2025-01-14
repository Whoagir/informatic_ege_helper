from itertools import *
a='ТИМАШЕВСК'
comb=product(a,repeat=6)
c=0
for i in comb:
    s=''.join(i)
    gl=s.count('И')+s.count('А')+s.count('Е')
    sogl=s.count('Т')+s.count('М')+s.count('Ш')+s.count('В')+s.count('С')+s.count('К')
    if gl<sogl and 'ТШ' not in s and 'ШТ'not in s and 'МШ'not in s and 'ШМ'not in s and 'ШШ' not in s and 'ВШ'not in s and'ШВ'not in s and 'СШ'not in s and'ШС' not in s and 'КШ' not in s and 'ШК' not in s:
        c+=1
print(c)