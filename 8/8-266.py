from itertools import product

A = sorted("ПЯТЬДНЕЙ")
allWords = [ "".join(w) for w in product(A, repeat=4) ]
ind = [ i+1 for i, w in enumerate(allWords)
                if w.count('Е') == 0 and w.count('Я') == 0 and
                  len(set(w)) == len(w) ]

print( max(ind) )

