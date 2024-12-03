from itertools import product

A = 'ЕГЭИНФ'
words = [''.join(w) for w in product(A, repeat=6)]
words = [ w for w in words 
            if w[0] == 'Е' and w[-1] in 'ЭИ' and 
            w.count('ФИ') == 2 and not('ЕГЭ' in w) ]

print( len(words) )

