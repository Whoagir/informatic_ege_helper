from itertools import product

A = 'ОБЩЕСТВ'
words = [''.join(w) for w in product(A, repeat=5)]
words = [ w for w in words
            if w[0] not in 'ЩБ' and w.endswith('ВВ') and
            'ТБ' in w and not('ЕВ' in w or 'ВЕ' in w) ]

print( len(words) )

