# Автор: Д. Статный

from itertools import product
#Комбинацию АНТИУТОПИЯ примем за *
k = 0
for x in product(set('АНТИУОПИЯ*'), repeat=7):
    s=''.join(x)
    vowels = [x for x in s if x in 'АИОУЯ']
    cons = [x for x in s if x in 'НТП']
    if vowels==sorted(vowels) and cons==sorted(cons)[::-1] and s.count('*')==1:
        k += 1
print(k)

