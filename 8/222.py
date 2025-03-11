from itertools import *
a='АЗНС'
c=1
comb=product(a,repeat=5)
for i in comb:
    s=''.join(i)
    c+=1
    if s=='САЗАН':
        v=c
    if s=='ЗАНАС':
        v1=c
print(v-v1+1)