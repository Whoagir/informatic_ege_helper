from itertools import *
a='ЧИУА'
c=0
comb=permutations(a,r=6)
for i in comb:
    s=''.join(i)
    c+=1
print(c)