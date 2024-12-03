# Автор: Л. Малинов

from itertools import permutations
k = 0
for x in permutations('КОМПЬЮТЕР'):
  s = ''.join(x)
  if s[0]<s[1]<s[2]<s[3] and s[-2] == 'Е':
    k += 1
print( k )