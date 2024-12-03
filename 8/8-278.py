# Автор: Л. Малинов

from itertools import product
k = 0
for x in product('ВИДЕО', repeat=6):
  s = "".join(x)
  vowels = [i for i in s if i in 'ИЕО']
  if s.count('И') >= 1 and s.count('Е') >= 1 and vowels == sorted(vowels):
    k += 1
print(k)