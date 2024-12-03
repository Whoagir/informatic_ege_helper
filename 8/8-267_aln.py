#8.267_Aвтор_А.Наймушин

from itertools import permutations

A = "СПОРТЛОТО"
allWords = [ "".join(w) for w in set( permutations(A)) ]
allWords = [ w for w in allWords if  w[-1] != 'О']

print( len(allWords) )

'''
20160
'''

