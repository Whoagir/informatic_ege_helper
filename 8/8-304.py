# Автор: Д. Статный

from itertools import product

#Комбинацию АНТИУТОПИЯ примем за *
k = 0
for x in product('АНТИУОПЯ*', repeat=7):
    s=''.join(x)
    vowels = [x for x in s if x in 'АИОУЯ']
    cons = [x for x in s if x in 'НТП']
    if vowels==sorted(vowels)[::-1] and cons==sorted(cons) and s.count('*')==1\
       and s.count('Т')+s.count('П')+s.count('Н')<=2:
        k += 1
print(k)
