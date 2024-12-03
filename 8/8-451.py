from itertools import product

A = sorted("АЭРОБУС")

count = 0
i = 1
for w in sorted(product(A, repeat=5)):
  s = ''.join(w)
  for c in "АЭОБУС":
    s = s.replace(c, '.')
  if i % 2 == 0 and 'Р.Р' in s and w.count('У') == 0:
    count += 1
  i += 1

print( count )