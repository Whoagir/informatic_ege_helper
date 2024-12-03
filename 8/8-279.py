# Автор: Л. Малинов

from itertools import permutations
k = 0
for x in set(permutations('ЭФЕКТ', r=5)):
  s = ''.join(x)
  consonant = [i for i in s if i in 'ФКТ' ]
  vowels = [i for i in s if i in 'ЭЕ']
  if consonant == sorted(consonant, reverse=True) and \
     vowels == sorted(vowels):
     k += 1
print(k)