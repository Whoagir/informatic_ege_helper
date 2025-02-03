from itertools import *
a='АГЕМНР'
c=0
comb=permutations(a,r=6)
for i in comb:
    s=''.join(i)
    c+=1
    if c==522:
        print(s)