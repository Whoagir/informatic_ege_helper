from itertools import product
A = set('ГЕРАКЛИТ')
G = 'ЕАИ'
gg = [ ''.join(x) for x in product(G, repeat=2) ]
S = A - set(G)

count = 0
for w in product(A, repeat=6):
  w = ''.join(w)
  if len(w) == len(set(w)) and \
     len([ wi for wi in w if wi in S ]) > len([ wi for wi in w if wi in G ]) and \
     all( x not in w for x in gg ):
     count += 1

print(count)




