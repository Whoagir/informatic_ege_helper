# Автор: Д. Статный

from itertools import product

#Комбинацию АНТИУТОПИЯ примем за *
k = 0
for x in product('АНТИУОПЯ*', repeat=7):
    s=''.join(x)
    right = ''
    left = ''
    #вычисление правой и левой части от комбинации
    for i in range(len(s)):
        if s[i]!='*':
            left += s[i]
        else:
            break
    right = s.replace(left+'*', '')
    rvowels = [x for x in right if x in 'АИУОЯ']
    rcons = [x for x in right if x in 'НТП']
    lvowels = [x for x in left if x in 'АИУОЯ']
    lcons = [x for x in left if x in 'НТП']
    if len(rvowels)==0 and rcons==sorted(rcons) and len(lcons)==0 and \
       lvowels==sorted(lvowels)[::-1] and s.count('*')==1 and len(right)!=0 and len(left)!=0:
        k+=1
print(k)

