from itertools import *
a='СПОРТЛОТО'
comb=product(a)
k=1
for i in comb:
    s=''.join(i)
    if s[0]!='О' and s[-1]!='О':
        k+=1
print(k)