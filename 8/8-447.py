from itertools import product

count = 0
i = 1
for w in product(sorted('КОМПАНИЯ'),repeat=6):
  s = ''.join(w)
  count += i % 2 == 1 and s[0] != 'М' and s.count('И') == 3
  i += 1

print( count )
