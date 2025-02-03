from itertools import *
a='0123456789'
c=0
comb=permutations(a,r=6)
for i in comb:
    s=''.join(i)
    if s[0]!='0' and (int(s[0])+int(s[1]))%2!=0 and (int(s[1])+int(s[2]))%2!=0 and (int(s[2])+int(s[3]))%2!=0 and (int(s[3])+int(s[4]))%2!=0 and (int(s[4])+int(s[5]))%2!=0:
        c+=1
print(c)