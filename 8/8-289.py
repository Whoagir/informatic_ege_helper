from itertools import product

prohibited = 'АЕИШ'

print( sum( w[0] not in prohibited
            for w in product( "ТИМАШЕВСК", repeat=4 ) ) )
