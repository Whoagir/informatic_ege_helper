from itertools import product

A = "КАЛЬКА"

words = product( A, repeat = 5 )
valid = [ x for x in words
            if x.count('А') <= 1 ]
print( len( set(valid) ) )
