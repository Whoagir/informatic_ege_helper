from itertools import product

words = list(product(sorted('ПРИВЫЧКА'), repeat = 5))
words = [ w for i, w in enumerate(words,start=1)
            if i % 5 != 0]
for i, w in enumerate(words,start=1):
  if all( c in "ПРВЧК" for c in w ) and len(w) == len(set(w)):
    print( i, w )
    break

# Автор: Д. Паршиков

from itertools import product
n = 0
for word in product(sorted('ПРИВЫЧКА'), repeat = 5):
   n += 1
   if n % 5 != 0 and len(set(word)) == 5 and all(x not in word for x in 'ИЫА'):
       print(n - n // 5)
       break