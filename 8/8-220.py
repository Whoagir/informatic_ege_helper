from itertools import permutations

A = 'СОТКАПЛЗ'

count = 0
for w in [''.join(x) for x in permutations(A, 5)]:
  if 'ЗЛО' not in w and w[-1] not in 'ОА':
    count += 1
    print(w)

print( count )

# Автор: А. Куканова

from itertools import permutations

WORD = 'СОТКАПЛЗ'
VOWELS = 'ОА'
words = [''.join(w) for w in permutations(WORD, r=5)]
words = [w for w in words if w[-1] not in VOWELS and 'ЗЛО' not in w]
print(len(words))