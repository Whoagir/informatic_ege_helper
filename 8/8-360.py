from itertools import product

lst = [ ''.join(w) for w in product(sorted(set('КРАТЕР')), repeat=6) ]

print( lst.index('РАКЕТА') - lst.index('КАРЕТА') - 1 )
