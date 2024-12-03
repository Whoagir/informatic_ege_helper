from itertools import product

print( sum( 1 for x in product('АНТИУОПЯ.', repeat=7)
                  if x.count('.') == 1) )
