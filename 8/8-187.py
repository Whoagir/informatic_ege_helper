from itertools import product

A = "БАНКИР"

words = product( A, repeat = 6 )
valid = [ x for x in words
            if x.count('А') <= 1 and x.count('И') <= 1 ]
print( len( set(valid) ) )
