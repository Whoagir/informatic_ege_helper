# Автор: П. Финкель

from itertools import*

a='АИЕ'
b='ТМШВСК'
k=0
for i in permutations('ТИМАШЕВСК'):
    x=''.join(i)
    for i in range(1,len(x)-3):
        if x[0] in b and x[-1] in b and x[i] in a and x[i+1] in a and x[i+2] in a:k+=1

print(k)
