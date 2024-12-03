from functools import lru_cache

A = 'CONST'
K = 16

@lru_cache(None)
def rec( A, cur, prev, steps ):
  if steps == 0:
     return 1 if cur != 'S' else 0
  count = 0
  for c in A:
    if not ( c == cur or (cur == 'S' and c == prev) ):
      count += rec( A, c, cur, steps-1 )
  return count

count = rec( A, 'S', ' ', K )

print( count )

""" # Второй вариант: через строки (медленный)
@lru_cache(None)
def recStr( A, s, steps ):
  if steps == 0:
     return 1 if s[-1] != 'S' else 0
  count = 0
  for c in A:
    if c != s[-1] and \
       not (s[-1] == 'S' and c == s[-2]):
      count += recStr( A, s+c, steps-1 )
  return count

count = recStr( A, ' S', K )

print( count )
"""

""" # Проверка для небольших K через генерацию всех возможных слов
from itertools import product
ban = [x+x for x in A] + [x+'S'+x for x in A]
count = 0
for word in [''.join(x) for x in product(A, repeat = K)]:
  if word[0] != 'S' and word[-1] != 'S' and \
     all( b not in word for b in ban ):
    count += 1

print( count )
"""

