from itertools import permutations

r = []
for w in permutations('КОБУРА'):
  w0 = ''.join(w)
  w = w0
  [w:=w.replace(c,'g') for c in 'ОУА']
  [w:=w.replace(c,'s') for c in 'КБР']
  if 'gg' not in w and 'ss' not in w:
    r.append(w0)

print( len(set(r)) )