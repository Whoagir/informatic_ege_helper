from itertools import product

N = 7
Nodd = 3
nOdd = len('1357')
nEven = len('0468') # 2 - особая цифра!

count = 0
for w in product('ЧН.', repeat=N):
  if w.count('.') == 1 and w.count('Н') == Nodd:
    if w[0] == 'Ч':
      count += nOdd**Nodd * (nEven-1) * nEven**(N-Nodd-2) * 1
    else:
      count += nOdd**Nodd * nEven**(N-Nodd-1) * 1

print( count )



