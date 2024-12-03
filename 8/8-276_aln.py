#8.276_Автор_A.Наймушин

from itertools import *
s = set()

for x in permutations ('СПОРТЛОТО'):
    word = ''.join(x)
    if 'ТТ' in word:
        s.add(word)
print (len(s)) 

'''
6720
'''
