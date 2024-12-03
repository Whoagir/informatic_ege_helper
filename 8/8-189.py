from itertools import product

A = "КОРНЕТ"

words = product( A, repeat = 5 )
valid = [ x for x in words
            if x.count('О') <= 1 and x.count('Е') <= 1 ]
print( len( set(valid) ) )
