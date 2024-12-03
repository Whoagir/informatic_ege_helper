# Автор: А. Родионов

from itertools import product

a=''.join(reversed(sorted('АЛГОРИТМ')))

k=8**5

for t in product(a, repeat= 5):
    s=''.join(t)
    if s[0]!='Т' and s.count('Г')==2 and k%2:
        print(k,s)
        break
    k-=1

