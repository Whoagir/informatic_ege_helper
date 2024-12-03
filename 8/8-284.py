from itertools import product

print( sum( 1 for x in product('АНТИУОПЯ.', repeat=7)
                  if x.count('.') == 1 and
                     x[0] not in ['А','.'] and
                     x[-1] not in ['Я', '.']) )
