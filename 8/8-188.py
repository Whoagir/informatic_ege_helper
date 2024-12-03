from itertools import product

A = "САКУРА"

words = product( A, repeat = 5 )
valid = [ x for x in words
            if x.count('А') <= 1 and x.count('У') <= 1 ]
print( len( set(valid) ) )
