from itertools import *
print(bin(255),bin(255),bin(192),'0b00000000')
print('0'+bin(102),bin(141),'0b00000000', '0b00000000')
a='01'
c=0
comb=product(a,repeat=14)
for i in comb:
    s=''.join(i)
    s='1'*18+s
    if s.count('1')%7==0 and s[-4::]=='1011':
        c+=1
print(c)