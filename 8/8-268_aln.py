#8.268_Автор_A.Наймушин

from itertools import permutations

A = "СПОРТЛОТО"
allWords = [ "".join(w) for w in set( permutations(A)) ]
allWords = [ w for w in allWords if  w[0] == 'О']

print( len(allWords) )

'''
10080
'''

