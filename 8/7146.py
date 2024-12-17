from itertools import product
s='ЭШЖГМТ'
comb=product (s,repeat=6)
c=0
for i in comb:
    s=''.join(i)
    shh=s.count('Ш')
    if shh==1:
        c+=1
print(c)
