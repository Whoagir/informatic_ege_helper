#8.274_Автор_A.Наймушин

from itertools import *
s = set()

for x in permutations ('СПОРТЛОТО'):
    word = ''.join(x)
    if 'ОО' in word:
        s.add(word)
print (len(s)) 

'''
17640
'''
