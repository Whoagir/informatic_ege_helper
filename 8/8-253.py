from itertools import product

A = 'ОГЭИНФ'
words = [''.join(w) for w in product(A, repeat=6)]
words = [ w for w in words 
            if w[0] in 'ЭО' and w.endswith('ФИ') and 
            'ИГ' in w and not('ОГЭ' in w) ]

print( len(words) )

