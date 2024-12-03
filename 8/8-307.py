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
    if s.count('*')==1 and len(rcons)==len(rvowels) and len(lcons)<=2:
        k+=1
print(k)



