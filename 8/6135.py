from itertools import *
a='ТИМОФЕЙ'
c=0
comb=product(a,repeat=6)
for i in comb:
    s=''.join(i)
    gl=s.count('И')+s.count('О')+s.count('Е')
    sogl=s.count('Т')+s.count('М')+s.count('Ф')+s.count('Й')
    if gl==sogl:
        c+=1
print(c)