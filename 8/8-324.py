# Автор: А. Кабанов

from itertools import product

N = 10
Nodd = 3
nOdd = len('1357')
nEven = len('0246')

count = 0
for w in product('ЧН', repeat=N):
  w = ''.join(w)
  if w.count('Н') == Nodd and 'НН' not in w:
    if w[0] == 'Ч':
      count += (nEven-1) * nEven**(N-Nodd-1) * nOdd**Nodd
    else:
      count += nEven**(N-Nodd) * nOdd**Nodd

print( count )
