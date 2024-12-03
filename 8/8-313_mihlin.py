'''
8.313 (C. Якунин) Дмитрий составляет слова, переставляя буквы в слове АМФИБРАХИЙ.
Сколько РАЗЛИЧНЫХ слов, в которых есть, хотя бы, 2 подряд идущие гласные может составить Дмитрий?
'''
from itertools import *
r={x for x in permutations('АМФИБРАХИЙ') if any(x[i] in 'АИ' and x[i+1] in 'АИ' for i in range(9))}
print(len(r)) # 756000 # Сколько РАЗЛИЧНЫХ слов, ...
#r=[x for x in permutations('АМФИБРАХИЙ') if any(x[i] in 'АИ' and x[i+1] in 'АИ' for i in range(9))]
#print(len(r)) # 3024000 