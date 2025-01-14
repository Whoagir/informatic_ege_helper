from itertools import *
a='0123456789AB'
comb=product(a,repeat=5)
c=0
for i in comb:
    s=''.join(i)
    v=s.count('4')
    if s[0]!='0' and v==2 and '14' not in s and '41' not in s and '34' not in s and '43' not in s and '54' not in s and '45' not in s and '74' not in s and '47' not in s and '94' not in s and '49' not in s and 'B4' not in s and '4B' not in s:
        c+=1
print(c)