from itertools import product

A = 'ЕСТЕСТВО'
gl = 'ЕО'
count = 0
for w in set(product(A, repeat=8)):
  w = ''.join(w)
  if len( [c for c in w if c in gl] ) in [3,4]:
    w = w.replace( 'Е', 'О' )
    if 'ОО' not in w:
      count += 1
print( count )