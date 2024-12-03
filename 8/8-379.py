from itertools import product

r = []
for w in product('КОМПЕГЭ', repeat=6):
  w0 = ''.join(w)
  w = w0
  [w:=w.replace(c,'g') for c in 'ОЕЭ']
  [w:=w.replace(c,'s') for c in 'КМПГ']
  if w == 'gssssg':
    r.append(w0)

print( len(set(r)) )