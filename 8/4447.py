from itertools import *
a='МАРИНА'
comb=permutations(a)
c=0
for i in comb:
    s=''.join(i)
    if s[0]!='И' and s[0]!='А':
        c+=1
print(c)