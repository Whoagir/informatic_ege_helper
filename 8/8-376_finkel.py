# Автор: П. Финкель

from itertools import*

a='0246'
b='1357'
k=0
for i in product('01234567',repeat=8):
    x=''.join(i)
    for i in range(1,len(x)-3):
        if x[0] in a and x[-1] in a and x[0]!='0' and x[i] in b and x[i+1] in b and x[i+2] in b:
           k+=1
           break

print(k)
