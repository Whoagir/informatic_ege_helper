from itertools import product
a="0123456789AB"
comb=product(a,repeat=5)
c=0
for i in comb:
  s=''.join(i)
  t=s.count('7')
  v=s.count('9')
  v1=s.count('A')
  v2=s.count('B')
  if t==1 and (v1+v2+v)<=3 and s[0]!='0':
    c+=1
print(c)
