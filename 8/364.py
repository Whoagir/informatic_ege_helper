from itertools import *
a='ЩОГБА'
c=0
comb=product(a,repeat=6)
for i in comb:
    s=''.join(i)
    c+=1
    if s=='ОБЩАГА':
        print(c)
        break