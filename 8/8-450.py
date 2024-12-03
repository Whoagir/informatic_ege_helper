from itertools import product

A = sorted("ГЛУБИНА", reverse=True)

count = 0
i = 1
for w in sorted(product(A, repeat=6)):
  s = ''.join(w)
  for c in "ГЛУБИН":
    s = s.replace(c, '.')
  if i % 2 == 1 and 'А..А' in s and w.count('Н') > 1:
    count += 1
  i += 1

print( count )