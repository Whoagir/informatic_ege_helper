#8.275_Автор_A.Наймушин

from itertools import *
s = set()

for x in permutations ('СПОРТЛОТО'):
    word = ''.join(x)
    if 'ООО' in word:
        s.add(word)
print (len(s)) 

'''
2520
'''
